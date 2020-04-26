
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
    pool = multiprocessing.Pool(processes=1)


    while objectPt.getCheckerState() :
        endtime = datetime.datetime.now()
        if( ( (endtime - starttime).seconds > 600 ) or isFirstCheck ):
            isFirstCheck = False
            starttime = endtime
            pool.apply_async(sustainedChecker)

    pool.close()
    pool.terminate()
    pool.join()


def sustainedChecker():
    checkerPt = readdataconsumer.ReadDataConsumer()
    try:
        flag = checkerPt.connect_mq()
        if flag:
            signal.signal(signal.SIGINT, checkerPt.signalQuit)
            checkerPt.startConsumer()
    except:
        print "checkconsumer sustainedChecker consumer close rabbitmq server!!"
        path = os.getcwd()
        filePath = path + "/log/rabbitmq.log"
        fileHandle = open(filePath, mode='a+')
        now = datetime.datetime.now()
        fileHandle.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        fileHandle.write(":checkconsumer sustainedChecker rabbitmq close consumer \n")
        fileHandle.close()



#class CheckConsumer

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

        path = os.getcwd()
        filePath = path + "/log/rabbitmq.log"
        fileHandle = open(filePath, mode='a+')
        now = datetime.datetime.now()
        fileHandle.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        fileHandle.write(":checkconsumer stopChecked rabbitmq  consumer \n")
        fileHandle.close()


    def getCheckerState(self):
        return self.state


