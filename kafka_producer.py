from confluent_kafka import Producer
import ujson
import os
import time
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('KAFKA_BROKER_URL'))

conf = {
    'bootstrap.servers': os.getenv('KAFKA_BROKER_URL')
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
