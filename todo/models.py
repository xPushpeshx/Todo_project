import imp
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

    
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)