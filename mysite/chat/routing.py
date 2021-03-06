from django.urls import re_path
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.BoardConsumer),
]

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
            url(r'ws/chat/(?P<room_name>\w+)/$', consumers.BoardConsumer),
        ])
    ),

})
