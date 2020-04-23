
import time

import readdataconsumer
import multiprocessing
import os
import signal


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


class CheckConsumer:

    def __init__(self):
        self.state = True
        self.processObj = None
        self.consumerObject = None


    def startChecked(self):
        self.consumerObject = readdataconsumer.ReadDataConsumer()
        self.processObj = multiprocessing.Process(target=execute, args=(self.consumerObject,self))
        self.processObj.start()

        #signal.signal(signal.SIGINT, self.stopChecked)


    def continueChecked(self):
        print "checkconsumer continueChecked is restart=",self.consumerObject.getallowConsumer()
        if (self.consumerObject.getallowConsumer() and self.state ):
            time.sleep(2)
            self.startChecked()


    def stopChecked(self,signal,frame):
        self.state = False




