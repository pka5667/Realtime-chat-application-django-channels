from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.core.paginator import Paginator


# Create your views here.
@login_required
def chatRoom(request):
    chat_messages = ChatMessage.objects.all().order_by('time')
    messages = Paginator(chat_messages, 20, 19)
    messages = messages.get_page(messages.num_pages)
    return render(request, 'chat/chatroom.html', {'chat_messages': list(messages)})
