# pylint: disable=W0311

# import the logging library
import logging

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Orden
from .tasks import calc_precio

# Get an instance of a logger
logger = logging.getLogger(__name__)

@receiver(post_save, sender=Orden)
def send_email_per_item(sender, instance, **kwargs):
  if instance.precio == 0:
    #calc_precio.delay(sender)
    calc_precio(instance)
    logger.info("Se calculara el precio")
