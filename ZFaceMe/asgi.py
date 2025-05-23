"""
ASGI config for ZFaceMe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from videochat import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ZFaceMe.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
   
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
    ))
})