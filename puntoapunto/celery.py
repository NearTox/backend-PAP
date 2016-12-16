from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puntoapunto.settings')
app = Celery('puntoapunto')


# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

try:
  from .local_settings import *
except ImportError:
  app.conf.update(
      BROKER_URL=os.environ['REDIS_URL'],
      CELERY_RESULT_BACKEND=os.environ['REDIS_URL']
  )

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

