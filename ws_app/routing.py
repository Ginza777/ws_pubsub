from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from .consumers import WsPubsubConsumer  # Make sure you import your consumer



websocket_urlpatterns = [
    re_path(r'ws/$', WsPubsubConsumer.as_asgi()),
]
