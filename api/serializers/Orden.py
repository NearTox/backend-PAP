# pylint: disable=W0311, C0111
from rest_framework import serializers
from core.models import (Orden, Cliente)

class OrdenSerializerGET(serializers.ModelSerializer):
  class Meta:
    model = Orden
    fields = '__all__'

class OrdenSerializerPATCH(serializers.ModelSerializer):
  latitud_origen = serializers.FloatField(required=False, min_value=-180.0, max_value=180.0)
  longitud_origen = serializers.FloatField(required=False, min_value=-180.0, max_value=180.0)
  latitud_destino = serializers.FloatField(required=False, min_value=-180.0, max_value=180.0)
  longitud_destino = serializers.FloatField(required=False, min_value=-180.0, max_value=180.0)
  detalles = serializers.CharField(required=False)
  #estado =

  cliente = serializers.SlugRelatedField(
      slug_field='id',
      many=False,
      queryset=Cliente.objects.all(),
      read_only=False,
      required=False)

  class Meta:
    model = Orden
    exclude = ('id', 'precio')

class OrdenSerializerNEW(serializers.ModelSerializer):
  latitud_origen = serializers.FloatField(required=True, min_value=-180.0, max_value=180.0)
  longitud_origen = serializers.FloatField(required=True, min_value=-180.0, max_value=180.0)
  latitud_destino = serializers.FloatField(required=True, min_value=-180.0, max_value=180.0)
  longitud_destino = serializers.FloatField(required=True, min_value=-180.0, max_value=180.0)
  detalles = serializers.CharField()
  #estado =

  cliente = serializers.SlugRelatedField(
      slug_field='id',
      many=False,
      queryset=Cliente.objects.all(),
      read_only=False,
      required=False)

  class Meta:
    model = Orden
    exclude = ('precio',)

