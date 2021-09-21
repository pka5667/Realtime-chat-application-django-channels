from django.urls import path

from .views import dashboard, profileView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('user/<str:username>', profileView, name='profile'),
]
