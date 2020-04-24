
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
        signal.signal(signal.SIGINT, consumerObj.signalQuit)
        if flag:
            consumerObj.startConsumer()
    except:
        print "checkconsumer execute consumer close rabbitmq server!!"
        checkerObj.continueChecked()


def executeCheck():
    checkerObject = readdataconsumer.ReadDataConsumer()
    while checkerObject.getallowConsumer() :
        try:
            flag = checkerObject.connect_mq()
            signal.signal(signal.SIGINT, checkerObject.signalQuit)
            if flag:
                checkerObject.startConsumer()
        except:
            print "checkconsumer executeCheck consumer close rabbitmq server!!"
            path = os.getcwd()
            filePath = path + "/log/rabbitmq.log"
            fileHandle = open(filePath, mode='a+')
            #fileHandle.write("pid:" + str(os.getpid()) + " ")
            now = datetime.datetime.now()
            fileHandle.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            fileHandle.write(":executeCheck consumer close rabbitmq  server\n")
            fileHandle.close()



class CheckConsumer:

    def __init__(self):
        self.state = True
        self.processObj = None
        self.consumerObject = None


    def startChecked(self):
        self.consumerObject = readdataconsumer.ReadDataConsumer()
        self.processObj = multiprocessing.Process(target=execute, args=(self.consumerObject,self))
        #self.processObj = multiprocessing.Process(target=executeCheck)
        self.processObj.start()

        #signal.signal(signal.SIGINT, self.stopChecked)


    def continueChecked(self):
        print "checkconsumer continueChecked is restart=",self.consumerObject.getallowConsumer()
        if (self.consumerObject.getallowConsumer() and self.state ):
            self.startChecked()


    def stopChecked(self,signal,frame):
        self.state = False




