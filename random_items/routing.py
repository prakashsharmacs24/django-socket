from channels.routing import ProtocolTypeRouter, URLRouter
from items.consumers import ItemsConsumer
from django.conf.urls import url

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        url("ws/items/", ItemsConsumer),
    ])
})
