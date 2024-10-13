from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from confluent_kafka import Producer
import ujson

# Create your views here.

def location(request):
    try:
        conf = {
            'bootstrap.servers': settings.KAFKA_BROKER_URL
        }
        producer = Producer(**conf)
        topic = 'location_update'
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        data = {
            'latitude': lat,
            'longitude': lon
        }
        def delivery_report(error, message):
            if error is not None:
                print(f"Message delivery failed: {error}")
            else:
                print(f"Message Delivered in: {message.topic()} [{message.partition}]")
        producer.produce(topic, ujson.dumps(data).encode('utf-8'), callback = delivery_report)
        producer.flush()
        print(lat,',', lon)
        return JsonResponse(data={
            'status': 200
        })
    except Exception as e:
        return JsonResponse(data={
            'status': 404,
            'error': e
        })

def home(request):
    
    return render(request, 'home.html')