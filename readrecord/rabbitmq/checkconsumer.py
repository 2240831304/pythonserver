
import time

import readdataconsumer
import multiprocessing
import os
import signal
import datetime
import threading


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



def pauseConsumer(pt):
    try:
        pt.quit()
    except Exception as e:
        print "checkconsumer pauseConsumer error:",e


def execute():
    checkerPt = readdataconsumer.ReadDataConsumer()
    try:
        flag = checkerPt.connect_mq()
    except Exception as e:
        print "checkconsumer execute stop consumer error:", e

    if flag:
        timer = threading.Timer(300, pauseConsumer,(checkerPt,))
        timer.start()
        checkerPt.startConsumer()

    checkerPt.stopRunConsumer()

    # path = os.getcwd()
    # filePath = path + "/log/rabbitmq.log"
    # fileHandle = open(filePath, mode='a+')
    # now = datetime.datetime.now()
    # fileHandle.write(now.strftime("%Y-%m-%d %H:%M:%S"))
    # fileHandle.write(":checkconsumer execute consumer close rabbitmq server!! \n")
    # fileHandle.close()

    timer = threading.Timer(600, execute)
    timer.start()


#class CheckConsumer

class CheckConsumer:

    def __init__(self):
        self.state = True
        self.processObj = None


    def startChecked(self):
        timer = threading.Timer(3, execute)
        timer.start()


    def stopChecked(self):
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


