"""
ASGI config for config_kafka_realtime project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.urls import re_path

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from delivery.routings import delivery_socket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config_kafka_realtime.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({

    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        application=AuthMiddlewareStack(
            URLRouter(delivery_socket_urlpatterns)
        )
    ),

})
