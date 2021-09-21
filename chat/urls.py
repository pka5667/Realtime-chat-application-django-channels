from django.urls import path

from .views import chatRoom

urlpatterns = [
    path('', chatRoom, name='chatRoom')
]
