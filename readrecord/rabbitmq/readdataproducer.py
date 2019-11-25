# -*- coding: utf-8 -*-

import pika


hostname = 'localhost'
queueName = 'ReadDataQueue'
exchangeName = 'ReadDataExchanger'
rountingKey = 'ReadDataKey'


class ReadDataProducer:

    def __init__(self):
        self.channel = None
        self.connection = None


    def connect_mq(self):
        credentials = pika.PlainCredentials(username='guest', password='guest')
        parameters = pika.ConnectionParameters(host=hostname, credentials=credentials)

        try:
            self.connection = pika.BlockingConnection(parameters)
        except Exception as e:
            print ("ReadDataProducer connect_mq:",e)
            return False

        flag = self.channel_mq()
        return flag


    def channel_mq(self):

        try:
            self.channel = self.connection.channel()
            # self.channel.queue_declare(queue=queueName,durable=True)

            self.channel.exchange_declare(exchange=exchangeName, durable=True, exchange_type='direct')

        except Exception as e:
            print ("ReadDataProducer channel_mq:", e)
            return False

        return True


    def addTask(self,data):
        self.channel.basic_publish(exchange=exchangeName, routing_key=rountingKey, body=data
                                   , properties=pika.BasicProperties(delivery_mode=2))

    def quit(self):
        self.channel.close()
        self.connection.close()