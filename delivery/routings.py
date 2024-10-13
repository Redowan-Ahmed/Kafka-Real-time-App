from django.urls import path

from .consumers import DeliveryLocationUpdate

delivery_socket_urlpatterns = [
    path(route="ws/live-location/<str:room_name>/", view=DeliveryLocationUpdate.as_asgi()),
]