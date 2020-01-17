# -*- coding: utf-8 -*-

import os
import django
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jiekou.settings')
django.setup()

import pika
import json
from readrecord.models import readprogress,bookreaddata,timeperioddata
from django.db.models import Sum,Max,Min
# from multiprocessing import Process
from readrecord.readdataprovide import readtimeprovide


hostname = 'localhost'
queueName = 'ReadDataQueue'
exchangeName = 'ReadDataExchanger'
rountingKey = 'ReadDataKey'
periodQueueName = 'PeriodReadDataQueue'


class ReadDataConsumer:

    def __init__(self):
        # Process.__init__(self)
        self.channel = None
        self.connection = None

    def run(self):
        self.startConsumer()


    '''
    def run(self):
        flag = self.connect_mq()
        if flag:
            self.startConsumer()
        else:
            print ("ReadDataConsumer create read data consumer is faile!!!!!!")
    '''


    def connect_mq(self):
        credentials = pika.PlainCredentials(username='guest', password='guest')
        parameters = pika.ConnectionParameters(host=hostname, credentials=credentials)

        try:
            self.connection = pika.BlockingConnection(parameters)
        except Exception as e:
            print ("ReadDataConsumer connect_mq:",e)
            return False

        flag = self.channel_mq()
        return flag


    def channel_mq(self):

        try:
            self.channel = self.connection.channel()
            self.channel.basic_qos(prefetch_count=1)

            self.channel.exchange_declare(exchange=exchangeName, durable=True, exchange_type='direct')

            self.channel.queue_declare(queue=queueName, durable=True)
            self.channel.queue_bind(exchange=exchangeName, queue=queueName, routing_key=rountingKey)
            self.channel.basic_consume(queueName, self.callback, consumer_tag="hello-consumer")

            # self.channel.queue_declare(queue=periodQueueName, durable=True)
            # self.channel.queue_bind(exchange=exchangeName, queue=periodQueueName, routing_key=rountingKey)
            # self.channel.basic_consume(periodQueueName, self.perioddatacallback, consumer_tag="consumer")

        except Exception as e:
            print ("ReadDataConsumer channel_mq:", e)
            return False

        return True


    def startConsumer(self):
        self.channel.start_consuming()


    def addQueue(self,name,rountKey):
        self.channel.queue_declare(queue=name, durable=True)
        self.channel.queue_bind(exchange=exchangeName, queue=name, routing_key=rountKey)
        self.channel.basic_consume(name, self.callback)


    def callback(self,ch, method, properties, body):
        dict = json.loads(body)
        # print ("ReadDataConsumer callback ,,callback======%r" % dict)
        #bookInfo = readprogress.objects.filter(serial=dict['serial'], bookName=dict['bookName'], bookId=dict['bookId']) \
        #    .aggregate(progressMax=Max('progress'), timeCount=Sum('readTime'), wordCount=Sum('wordCount'))

        bookInfo = readprogress.objects.filter(serial=dict['serial'], bookName=dict['bookName'], bookId=dict['bookId']) \
           .aggregate(progressMax=Max('progress'))

        try:
            saveObject = bookreaddata.objects.get(serial=dict['serial'], bookName=dict['bookName'], readdate=dict['readDate'])
            saveObject.dayreadtime = saveObject.dayreadtime + dict['readTime']
            saveObject.dayreadword = saveObject.dayreadword + dict['readWord']
        except bookreaddata.DoesNotExist:
            saveObject = bookreaddata()
            saveObject.dayreadtime = dict['readTime']
            saveObject.dayreadword = dict['readWord']

            try:
                recordInfo = bookreaddata.objects.filter(serial=dict['serial']).aggregate(maxRecord=Max('record'))
                saveObject.record = recordInfo['maxRecord'] + 1
            except:
                saveObject.record = 1

        #progressInfo = readprogress.objects.filter(serial=dict['serial'], bookName=dict['bookName'], startTime=dict['readDate'])\
        #    .aggregate(progressMax=Max('progress'), progressMin=Min('dayminprogress'))
        #saveObject.daymaxprogress = progressInfo['progressMax']
        #saveObject.dayminprogress = progressInfo['progressMin']
        #saveObject.dayreadprogress = saveObject.daymaxprogress - saveObject.dayminprogress

        saveObject.serial = dict['serial']
        saveObject.bookName = dict['bookName']
        saveObject.bookId = dict['bookId']
        saveObject.readdate = dict['readDate']
        #saveObject.wordcount = bookInfo['wordCount']
        #saveObject.timecount = bookInfo['timeCount']
        saveObject.wordcount = 0
        saveObject.timecount = 0
        saveObject.maxprogress = bookInfo['progressMax']
        saveObject.state = True

        saveObject.save()

        ch.basic_ack(delivery_tag=method.delivery_tag)


    def perioddatacallback(self,ch, method, properties, body):
        dict = json.loads(body)

        resultCode, todaydateList = readtimeprovide.getTodayReadWordTime(dict['serial'])
        resultCode, weekdateList = readtimeprovide.getWeekReadWordTime(dict['serial'])
        resultCode, monthdateList = readtimeprovide.getMonthReadWordTime(dict['serial'])
        resultCode, yeardateList = readtimeprovide.getYearReadWordTime(dict['serial'])
        resultCode, totledateList = readtimeprovide.getTotleReadWordTime(dict['serial'])

        try:
            saveObject = timeperioddata.objects.get(serial=dict['serial'])
        except timeperioddata.DoesNotExist:
            saveObject = timeperioddata()

        if todaydateList['wordCount'] == None:
            saveObject.todayword = 0
        else:
            saveObject.todayword = todaydateList['wordCount']

        if todaydateList['timeCount'] == None:
            saveObject.todaytime = 0
        else:
            saveObject.todaytime = todaydateList['timeCount']

        if weekdateList['wordCount'] == None:
            saveObject.weekword = 0
        else:
            saveObject.weekword = weekdateList['wordCount']

        if weekdateList['timeCount'] == None:
            saveObject.weektime = 0
        else:
            saveObject.weektime = weekdateList['timeCount']

        if monthdateList['wordCount'] == None:
            saveObject.monthword = 0
        else:
            saveObject.monthword = monthdateList['wordCount']

        if monthdateList['timeCount'] == None:
            saveObject.monthtime = 0
        else:
            saveObject.monthtime = monthdateList['timeCount']

        if yeardateList['wordCount'] == None:
            saveObject.yearword = 0
        else:
            saveObject.yearword = yeardateList['wordCount']

        if yeardateList['timeCount'] == None:
            saveObject.yeartime = 0
        else:
            saveObject.yeartime = yeardateList['timeCount']

        if totledateList['wordCount'] == None:
            saveObject.totleword = 0
        else:
            saveObject.totleword = totledateList['wordCount']

        if totledateList['timeCount'] == None:
            saveObject.totletime = 0
        else:
            saveObject.totletime = totledateList['timeCount']

        saveObject.serial = dict['serial']
        saveObject.save()

        ch.basic_ack(delivery_tag=method.delivery_tag)


    def quit(self):
        self.channel.stop_consuming(queueName)

    def signalQuit(self,signum, frame):
        self.channel.stop_consuming(queueName)
        # self.channel.stop_consuming(periodQueueName)


if __name__ == '__main__':
    object = ReadDataConsumer()
    # object.connect_mq()
    # object.addQueue("SecondQUeue","testKey")
    flag = object.connect_mq()
    if flag:
        object.startConsumer()