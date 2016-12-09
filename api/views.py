from django.shortcuts import render
from rest_framework import viewsets
from core.models import DatosPostales
from .serializer import (
    DatosPostalesSerializer,
)
# Create your views here.

class DatosPostalesViewSet(viewsets.ModelViewSet):
  """Detalles del usuario"""
  queryset = DatosPostales.objects.all()
  def get_serializer_class(self):
    if self.action == 'list':
      return DatosPostalesSerializerGET
    elif self.action == 'partial_update':
      return DatosPostalesSerializerPOST
    else:
      return DatosPostalesSerializerNEW