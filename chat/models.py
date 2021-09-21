from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ChatMessage(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)
