"""from .user_function import *
from .middleware import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save,post_init,post_migrate
from django.dispatch import receiver


@receiver(post_init, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
"""