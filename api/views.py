from django.shortcuts import render
from rest_framework import viewsets
from core.models import (DatosPostales, Cliente, Mensajero, Orden)
from .serializer import (
    DatosPostalesSerializer,
    MensajeroSerializer,
    ClienteSerializer,
    OrdenSerializer,
)
# Create your views here.

class DatosPostalesViewSet(viewsets.ModelViewSet):
  """Detalles del usuario"""
  queryset = DatosPostales.objects.all()
  serializer_class = DatosPostalesSerializer
  """def get_serializer_class(self):
    if self.action == 'list':
      return DatosPostalesSerializerGET
    elif self.action == 'partial_update':
      return DatosPostalesSerializerPOST
    else:
      return DatosPostalesSerializerNEW"""

class MensajeroViewSet(viewsets.ModelViewSet):
  """Detalles del Mensajero"""
  queryset = Mensajero.objects.all()
  serializer_class = MensajeroSerializer
  """def get_serializer_class(self):
    if self.action == 'list':
      return DatosPostalesSerializerGET
    elif self.action == 'partial_update':
      return DatosPostalesSerializerPOST
    else:
      return DatosPostalesSerializerNEW"""

class ClienteViewSet(viewsets.ModelViewSet):
  """Detalles del Cliente"""
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer
  """def get_serializer_class(self):
    if self.action == 'list':
      return DatosPostalesSerializerGET
    elif self.action == 'partial_update':
      return DatosPostalesSerializerPOST
    else:
      return DatosPostalesSerializerNEW"""

class OrdenViewSet(viewsets.ModelViewSet):
  """Detalles de la Orden"""
  queryset = Orden.objects.all()
  serializer_class = OrdenSerializer
  """def get_serializer_class(self):
    if self.action == 'list':
      return DatosPostalesSerializerGET
    elif self.action == 'partial_update':
      return DatosPostalesSerializerPOST
    else:
      return DatosPostalesSerializerNEW"""
