from __future__ import unicode_literals

from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models import signals
from tastypie.models import create_api_key

class ServicesConfig(AppConfig):
    name = 'services'

    def ready(self):
       # This line dispatches signal to Tastypie to create APIKey
       signals.post_save.connect(create_api_key, sender=User)
