import pika

params = pika.URLParameters("amqps://tmgmrdcf:qjgjxvX7aESgpI2NnzRRWeKrLgq9fLsB@shark.rmq.cloudamqp.com/tmgmrdcf")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue="admin", on_message_callback=callback)


print("Consumption successful")

channel.start_consuming()

channel.close()