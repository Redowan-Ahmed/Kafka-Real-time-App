from confluent_kafka import Producer
import ujson
import os
import time

conf = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(**conf)
topic = 'location_update'
number = 100


def delivery_report(error, message):
    if error is not None:
        print(f"Message delivery failed: {error}")
    else:
        print(f"Message Delivered in: {message.topic()} [{message.partition}]")

while number < 2000:
    data = {
        'position': number
    }
    print(data)

    producer.produce(topic, ujson.dumps(data).encode('utf-8'), callback = delivery_report)
    producer.flush()
    number+= 1

    time.sleep(1)
