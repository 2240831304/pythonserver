 # -*- coding: utf-8 -*-

import pika
import random

hostname = 'localhost'
queueName = 'ReadDataQueue'
exchangeName = 'ReadDataExchanger'
rountingKey = 'ReadDataKey'

# 新建连接，rabbitmq安装在本地则hostname为'localhost'
hostname = 'localhost'
credentials = pika.PlainCredentials(username='guest', password='guest')
parameters = pika.ConnectionParameters(host=hostname,credentials=credentials)
#parameters = pika.ConnectionParameters(host=hostname)
connection = pika.BlockingConnection(parameters)

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))

# 创建通道
channel = connection.channel()
channel.exchange_declare(exchange = exchangeName,durable = True, exchange_type='direct')
# 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
# channel.queue_declare(queue='ReadDataQueue',durable=True)
# channel.queue_declare(queue='ReadDataQueue')

number = random.randint(1, 1000)
body = 'hello world:%s' % number
# 交换机; 队列名,写明将消息发往哪个队列; 消息内容
# routing_key在使用匿名交换机的时候才需要指定，表示发送到哪个队列
channel.basic_publish(exchange=exchangeName, routing_key=rountingKey,
                      body=body,properties=pika.BasicProperties(delivery_mode=2))
print " [x] Sent %s" % body
connection.close()