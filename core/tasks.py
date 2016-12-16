# pylint: disable=W0311
from __future__ import absolute_import, unicode_literals

from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
from requests.exceptions import (RequestException, HTTPError)
from requests import get as requests_get
from .fuctions import get_precio

logger = get_task_logger(__name__)

url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
headers = {'Accept', 'application/json;*/*'}

@task(name="calc_precio")
def calc_precio(orden):
  params = {
      "origin": "{0},{1}".format(
          orden.latitud_origen,
          orden.longitud_origen,
      ),
      "destination": "{0},{1}".format(
          orden.latitud_destino,
          orden.longitud_destino,
      ),
      "api-key": "AIzaSyBo5GkfGaDY3Vfhz-nMwf4oWemPj6uUdUQ",
  }
  try:
    resp = requests_get(url=url, params=params, headers=headers)
    data = resp.json()
    element = data.rows[0].elements[0]
    resultado = get_precio(orden.peso_del_paquete, element.distance.value)
    if resultado[0]:
      logger.info(
          "La tarifa del servicio es de ${} pesos".format(
              format(resultado[1], ".2f")
          )
      )
      orden.precio = resultado[1]
    else:
      logger.warn(resultado[1])
  except (RequestException, ValueError, HTTPError):
    pass
  pass
