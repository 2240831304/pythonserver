

# -*- coding: utf-8 -*-

import pika

hostname = 'localhost'
queueName = 'ReadDataQueue'
exchangeName = 'ReadDataExchanger'
rountingKey = 'ReadDataKey'


credentials = pika.PlainCredentials(username='guest', password='guest')
parameters = pika.ConnectionParameters(host=hostname,credentials=credentials)
#parameters = pika.ConnectionParameters(host=hostname)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.basic_qos(prefetch_count=1)
channel.exchange_declare(exchange = exchangeName,durable = True, exchange_type='direct')

channel.queue_declare(queue=queueName,durable=True)
channel.queue_bind(exchange = exchangeName,queue = queueName,routing_key=rountingKey)

# channel.queue_declare(queue='ReadDataQueue')


def callback(ch, method, properties, body):

    print ("callback ,,callback======%r" % body)

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queueName,callback, consumer_tag="hello-consumer")
# channel.basic_consume(callback,'hello')



# di er ge dui lie
# channel12 = connection.channel()
channel.queue_declare(queue='SecondQueue',durable=True)
# channel12.basic_qos(prefetch_count=1)
# channel12.exchange_declare(exchange = exchangeName,durable = True, exchange_type='direct')
channel.queue_bind(exchange = exchangeName,queue = 'SecondQueue',routing_key=rountingKey)

def callback2(ch, method, properties, body):

    print ("callback2,,,,callback2======%r" % body)

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume('SecondQueue',callback2)


channel.start_consuming()
# channel12.start_consuming()

