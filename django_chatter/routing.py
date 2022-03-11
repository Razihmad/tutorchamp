from django.urls import path

from . import consumers

websocket_urlpatterns = [
	path('ws/django_chatter/chatrooms/<str:room_uuid>/', consumers.ChatConsumer.as_asgi()),
	path('ws/django_chatter/users/<str:username>/', consumers.AlertConsumer.as_asgi())
]
