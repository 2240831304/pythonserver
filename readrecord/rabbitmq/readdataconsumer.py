# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jiekou.settings')
django.setup()

import pika
import json
from readrecord.models import readprogress,bookreaddata
from django.db.models import Sum,Max
from multiprocessing import Process


hostname = 'localhost'
queueName = 'ReadDataQueue'
exchangeName = 'ReadDataExchanger'
rountingKey = 'ReadDataKey'



class ReadDataConsumer(Process):

    def __init__(self):
        Process.__init__(self)
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
        print ("ReadDataConsumer callback ,,callback======%r" % dict)
        bookIndfo = readprogress.objects.filter(serial=dict['serial'], bookName=dict['bookName'], bookId=dict['bookId']) \
            .aggregate(progressMax=Max('progress'), timeCount=Sum('readTime'), wordCount=Sum('wordCount'))

        try:
            saveObject = bookreaddata.objects.get(serial=dict['serial'], bookName=dict['bookName'], bookId=dict['bookId'])
        except bookreaddata.DoesNotExist:
            saveObject = bookreaddata()

        saveObject.serial = dict['serial']
        saveObject.bookName = dict['bookName']
        saveObject.bookId = dict['bookId']
        saveObject.wordcount = bookIndfo['wordCount']
        saveObject.timecount = bookIndfo['timeCount']
        saveObject.maxprogress = bookIndfo['progressMax']

        saveObject.save()

        ch.basic_ack(delivery_tag=method.delivery_tag)


    def quit(self):
        self.channel.stop_consuming()



if __name__ == '__main__':
    object = ReadDataConsumer()
    # object.connect_mq()
    # object.addQueue("SecondQUeue","testKey")
    object.start()
