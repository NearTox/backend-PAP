# pylint: disable=W0311
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class DatosPostales(models.Model):
  #Fields
  nombre = models.CharField(blank=False, max_length=250)
  telefono = PhoneNumberField()
  email = models.EmailField(blank=False, max_length=200)
  calle = models.CharField(blank=False, max_length=250)
  numero_exterior = models.CharField(blank=False, max_length=250)
  numero_interior = models.CharField(max_length=250)
  colonia = models.CharField(blank=False, max_length=250)
  c_p = models.IntegerField()
  delegacion = models.CharField(blank=False, max_length=250)
  estado = models.CharField(blank=False, max_length=250)
  pais = models.CharField(blank=False, max_length=250)

  #Relations
  #usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.nombre + " " + self.calle

class Cliente(models.Model):
  nombre = models.CharField(blank=False, max_length=250)
  email = models.EmailField(blank=False, max_length=200)
  telefono = PhoneNumberField()
  class Meta:
    unique_together = ('nombre', 'email', 'telefono')

class Orden(models.Model):
  latitud_origen = models.FloatField()
  longitud_origen = models.FloatField()
  latitud_destino = models.FloatField()
  longitud_destino = models.FloatField()
  precio = models.FloatField(default=0)
  detalles = models.TextField()
  #estado =

  cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL)
  mensajero = models.ForeignKey('Mensajero', blank=True, null=True, on_delete=models.SET_NULL)

  def update_precio(self):
    #make the price
    pass

class Mensajero(models.Model):
  nombre = models.CharField(blank=False, max_length=250)
  telefono = PhoneNumberField()

  class Meta:
    unique_together = ('nombre', 'telefono')

