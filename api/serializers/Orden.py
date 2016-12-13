# pylint: disable=W0311, C0111
from rest_framework import serializers
from core.models import (Orden, Cliente)
from .Cliente import ClienteSerializerGET
class OrdenSerializerGET(serializers.ModelSerializer):
  cliente = ClienteSerializerGET(many=False, read_only=True)
  class Meta:
    model = Orden
    fields = '__all__'

class OrdenSerializerPATCH(serializers.ModelSerializer):
  latitud_mensajero = serializers.DecimalField(required=False, min_value=-180.0, max_value=180.0, default=0, max_digits=13, decimal_places=10)
  longitud_mensajero = serializers.DecimalField(required=False, min_value=-180.0, max_value=180.0, default=0, max_digits=13, decimal_places=10)
  
  observaciones = serializers.CharField(required=False)
  #estado =

  cliente = serializers.SlugRelatedField(
      slug_field='id',
      many=False,
      queryset=Cliente.objects.all(),
      read_only=False,
      allow_null=True,
      required=False)

  class Meta:
    model = Orden
    exclude = (
        'precio', 'mensajero',
        'latitud_origen', 'longitud_origen',
        'latitud_destino', 'longitud_destino',)

class OrdenSerializerNEW(serializers.ModelSerializer):
  latitud_origen = serializers.DecimalField(
      required=True, min_value=-180.0, max_value=180.0,
      max_digits=13, decimal_places=10)
  longitud_origen = serializers.DecimalField(
      required=True, min_value=-180.0, max_value=180.0,
      max_digits=13, decimal_places=10)

  latitud_destino = serializers.DecimalField(
      required=True, min_value=-180.0, max_value=180.0,
      max_digits=13, decimal_places=10)
  longitud_destino = serializers.DecimalField(
      required=True, min_value=-180.0, max_value=180.0,
      max_digits=13, decimal_places=10)

  observaciones = serializers.CharField()
  peso_del_paquete = serializers.DecimalField(
      required=True, min_value=0.100, max_value=25,
      max_digits=5, decimal_places=3)

  cliente = serializers.SlugRelatedField(
      slug_field='id',
      many=False,
      queryset=Cliente.objects.all(),
      read_only=False,
      allow_null=True,
      required=False)

  class Meta:
    model = Orden
    exclude = ('precio', 'latitud_mensajero', 'longitud_mensajero', 'mensajero',)

