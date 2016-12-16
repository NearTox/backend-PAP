# pylint: disable=W0311
from django.apps import AppConfig

class CoreConfig(AppConfig):
  name = 'core'
  def ready(self):
    import core.signals
