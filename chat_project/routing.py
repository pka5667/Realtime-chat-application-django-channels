import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

import django
django.setup()


from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing


application = ProtocolTypeRouter({
    #http is by default 
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.ws_patterns
        )
    )
})
