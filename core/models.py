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
  empresa = models.CharField(blank=True, null=True, max_length=250)
  nombre = models.CharField(blank=False, max_length=250)
  email = models.EmailField(blank=False, max_length=200)
  telefono = PhoneNumberField()

  class Meta:
    unique_together = ('nombre', 'email', 'telefono', 'empresa')

  def __str__(self):
    return self.nombre + " " + self.email #+ " " + self.telefono 

class Orden(models.Model):
  latitud_origen = models.DecimalField(max_digits=13, decimal_places=10)
  longitud_origen = models.DecimalField(max_digits=13, decimal_places=10)

  latitud_destino = models.DecimalField(max_digits=13, decimal_places=10)
  longitud_destino = models.DecimalField(max_digits=13, decimal_places=10)
  
  latitud_mensajero = models.DecimalField(default=0, max_digits=13, decimal_places=10)
  longitud_mensajero = models.DecimalField(default=0, max_digits=13, decimal_places=10)

  numero_interior = models.CharField(blank=True, null=True, max_length=200)
  peso_del_paquete = models.DecimalField(default=0.100, max_digits=5, decimal_places=3)
  observaciones = models.TextField()
  precio = models.DecimalField(default=0, max_digits=10, decimal_places=2)


  cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL)
  mensajero = models.ForeignKey('Mensajero', blank=True, null=True, on_delete=models.SET_NULL)

  def update_precio(self):
    #make the price
    pass

  def update_mensajero(self):
    #make the mensajero
    pass

  def __str__(self):
    return "Orden: {1} ".format(self.id)

class Mensajero(models.Model):
  nombre = models.CharField(blank=False, max_length=250)
  telefono = PhoneNumberField()

  class Meta:
    unique_together = ('nombre', 'telefono',)

  def __str__(self):
    return self.nombre
