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

            self.channel.exchange_declare(exchange=exchangeName, durable=True, exchange_type='direct')

            self.channel.queue_declare(queue=queueName, durable=True)
            self.channel.queue_bind(exchange=exchangeName, queue=queueName, routing_key=rountingKey)
            self.channel.basic_qos(prefetch_count=1)
            self.channel.basic_consume(queueName, self.callback,auto_ack=False,consumer_tag="hello-consumer")
            self.connection.process_data_events()

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

        saveObject.serial = dict['serial']
        saveObject.bookName = dict['bookName']
        saveObject.bookId = dict['bookId']
        saveObject.readdate = dict['readDate']
        if bookInfo['progressMax'] == None:
            saveObject.maxprogress = 0
        else:
            saveObject.maxprogress = bookInfo['progressMax']

        saveObject.state = True
        saveObject.endreadtime = dict["endreadtime"]

        try:
            saveObject.save()
        except:
            ch.basic_ack(delivery_tag=method.delivery_tag)

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
        self.channel.close()
        self.connection.close()
        # self.channel.stop_consuming(periodQueueName)


if __name__ == '__main__':
    object = ReadDataConsumer()
    # object.connect_mq()
    # object.addQueue("SecondQUeue","testKey")
    flag = object.connect_mq()
    if flag:
        object.startConsumer()