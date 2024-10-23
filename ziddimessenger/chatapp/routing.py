from django.urls import path
from .consumers import chatconsumer
ws_patterns=[
    path('stream/',chatconsumer.as_asgi())
]