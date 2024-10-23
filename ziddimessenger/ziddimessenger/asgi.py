"""
ASGI config for ziddimessenger project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import URLRouter,ProtocolTypeRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ziddimessenger.settings')
from chatapp.routing import ws_patterns
application = ProtocolTypeRouter({

'http':get_asgi_application(),
'websocket': URLRouter(ws_patterns),
})
