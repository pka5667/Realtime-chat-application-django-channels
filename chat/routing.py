from django.urls import re_path

from . import consumers

ws_patterns = [
    # we need to make only one public chat room 
    re_path(r'ws/chat/', consumers.ChatroomConsumer.as_asgi()),
]
