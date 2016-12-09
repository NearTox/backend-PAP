# pylint: disable=W0311
from django.db import models

# Create your models here.
class DatosPostales(models.Model):
  nombre = models.CharField(blank=False, max_length=250)
  calle = models.CharField(blank=False, max_length=250)
  numero_exterior = models.CharField(blank=False, max_length=250)
  numero_interior = models.CharField(max_length=250)
  colonia = models.CharField(blank=False, max_length=250)
  c_p = models.IntegerField()
  delegacion = models.CharField(blank=False, max_length=250)
  estado = models.CharField(blank=False, max_length=250)
  pais = models.CharField(blank=False, max_length=250)

