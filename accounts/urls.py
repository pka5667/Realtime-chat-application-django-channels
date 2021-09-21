from django.urls import path

from .views import registrationView, loginView, logoutView

urlpatterns = [
    path('login/', loginView, name='login'),
    path('registration/', registrationView, name='registration'),
    path('logout/', logoutView, name='logout'),
]
