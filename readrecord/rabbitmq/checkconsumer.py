
import time

import readdataconsumer
import multiprocessing
import os
import signal
import datetime


def execute(consumerObj,checkerObj):
    print "checkconsumer execute  start run consumer!!!!"
    try:
        flag = consumerObj.connect_mq()
        if flag:
            signal.signal(signal.SIGINT, consumerObj.signalQuit)
            consumerObj.startConsumer()
    except:
        print "checkconsumer execute consumer close rabbitmq server!!"
        checkerObj.continueChecked()


def executeCheck(objectPt):
    signal.signal(signal.SIGINT, objectPt.stopChecked)
    starttime = datetime.datetime.now()

    isFirstCheck = True
    pool = multiprocessing.Pool(processes=3)

    while objectPt.getCheckerState() :
        endtime = datetime.datetime.now()
        if( ( (endtime - starttime).seconds > 10 ) or isFirstCheck ):
            isFirstCheck = False
            starttime = endtime
            pool.apply_async(sustainedChecker)
            # processPt = multiprocessing.Process(target=sustainedChecker)
            # processPt.start()

    pool.close()
    pool.terminate()
    pool.join()


def sustainedChecker():
    try:
        checkerPt = readdataconsumer.ReadDataConsumer()
        flag = checkerPt.connect_mq()
        if flag:
            signal.signal(signal.SIGINT, checkerPt.signalQuit)
            checkerPt.startConsumer()
    except:
        print "checkconsumer sustainedChecker consumer close rabbitmq server!!"




class CheckConsumer:

    def __init__(self):
        self.state = True
        self.processObj = None
        self.consumerObject = None


    def startChecked(self):
        self.consumerObject = readdataconsumer.ReadDataConsumer()
        #self.processObj = multiprocessing.Process(target=execute, args=(self.consumerObject,self))
        self.processObj = multiprocessing.Process(target=executeCheck,args=(self,) )
        self.processObj.start()



    def continueChecked(self):
        print "checkconsumer continueChecked is restart=",self.consumerObject.getallowConsumer()
        if (self.consumerObject.getallowConsumer() and self.state ):
            self.startChecked()


    def stopChecked(self,signal,frame):
        self.state = False


    def getCheckerState(self):
        return self.state


