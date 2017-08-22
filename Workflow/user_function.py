import datetime
from django.contrib.auth.models import User
from django.core.cache import cache
from django.conf import settings

def last_seen(self):
        return cache.get('seen_%s' % user.username)

def online(self):
    if self.last_seen():
        now = datetime.datetime.now()
        if now > self.last_seen() + datetime.timedelta(
                        seconds=settings.USER_ONLINE_TIMEOUT):
            return False
        else:
            return True
    else:
        return False

User.add_to_class('last_seen',last_seen)
User.add_to_class('online',online)
