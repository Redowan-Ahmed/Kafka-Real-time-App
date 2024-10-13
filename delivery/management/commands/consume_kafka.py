from django.core.management.base import BaseCommand
from kafka_consumer import getLocation

class Command(BaseCommand):
    help = 'Run Kafka consumer'

    def handle(self, *args, **kwargs):
        getLocation()