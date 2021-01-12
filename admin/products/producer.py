# amqps://tmgmrdcf:qjgjxvX7aESgpI2NnzRRWeKrLgq9fLsB@shark.rmq.cloudamqp.com/tmgmrdcf

import pika, json

params = pika.URLParameters("amqps://tmgmrdcf:qjgjxvX7aESgpI2NnzRRWeKrLgq9fLsB@shark.rmq.cloudamqp.com/tmgmrdcf")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body), properties=properties)