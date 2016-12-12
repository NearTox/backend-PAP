from django.shortcuts import render
from rest_framework import viewsets
from core.models import (DatosPostales, Cliente, Mensajero, Orden)
from .serializers.DatosPostales import DatosPostalesSerializer
from .serializers.Mensajero import (MensajeroSerializerGET, MensajeroSerializerPATCH, MensajeroSerializerNEW)
from .serializers.Cliente import (ClienteSerializerGET, ClienteSerializerPATCH, ClienteSerializerNEW)
from .serializers.Orden import (OrdenSerializerGET, OrdenSerializerPATCH, OrdenSerializerNEW)
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
  def get_serializer_class(self):
    if self.action == 'list':
      return MensajeroSerializerGET
    elif self.action == 'partial_update':
      return MensajeroSerializerPATCH
    else:
      return MensajeroSerializerNEW

class ClienteViewSet(viewsets.ModelViewSet):
  """Detalles del Cliente"""
  queryset = Cliente.objects.all()
  def get_serializer_class(self):
    if self.action == 'list':
      return ClienteSerializerGET
    elif self.action == 'partial_update':
      return ClienteSerializerPATCH
    else:
      return ClienteSerializerNEW

class OrdenViewSet(viewsets.ModelViewSet):
  """Detalles de la Orden"""
  queryset = Orden.objects.all()
  def get_serializer_class(self):
    if self.action == 'list':
      return OrdenSerializerGET
    elif self.action == 'partial_update':
      return OrdenSerializerPATCH
    else:
      return OrdenSerializerNEW
