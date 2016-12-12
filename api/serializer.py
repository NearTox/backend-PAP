# pylint: disable=W0311, C0111
from rest_framework import serializers
from core.models import (DatosPostales, Cliente, Mensajero, Orden)
class DatosPostalesSerializer(serializers.ModelSerializer):
  class Meta:
    model = DatosPostales
    fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = '__all__'

class MensajeroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mensajero
    fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Orden
    fields = '__all__'
