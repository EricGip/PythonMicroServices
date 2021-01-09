# amqps://tmgmrdcf:qjgjxvX7aESgpI2NnzRRWeKrLgq9fLsB@shark.rmq.cloudamqp.com/tmgmrdcf

import pika

params = pika.URLParameters("amqps://tmgmrdcf:qjgjxvX7aESgpI2NnzRRWeKrLgq9fLsB@shark.rmq.cloudamqp.com/tmgmrdcf")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange="", routing_key="admin", body="hello")