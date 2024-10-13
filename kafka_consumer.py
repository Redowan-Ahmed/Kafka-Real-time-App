from kafka import KafkaConsumer
import ujson
from dotenv import load_dotenv
import os

load_dotenv()


def getLocation():
    consumer = KafkaConsumer(
        'location_update',
        bootstrap_servers= os.getenv('KAFKA_BROKER_URL'),
        value_deserializer=lambda m: ujson.loads(m.decode('utf-8'))
    )

    for message in consumer:
        print(message)
