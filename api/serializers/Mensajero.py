# pylint: disable=W0311, C0111
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from core.models import (Mensajero, Orden)
from .PhoneNumber import PhoneNumberSerializer


class MensajeroSerializerGET(serializers.ModelSerializer):
  class Meta:
    model = Mensajero
    fields = '__all__'

class MensajeroSerializerPATCH(serializers.ModelSerializer):
  nombre = serializers.CharField(required=False)
  telefono = PhoneNumberSerializer(required=False)
  
  class Meta:
    model = Mensajero
    exclude = ('id',)

class MensajeroSerializerNEW(serializers.ModelSerializer):
  nombre = serializers.CharField(required=True)
  telefono = PhoneNumberSerializer(required=True)

  class Meta:
    model = Mensajero
    fields = '__all__'
    validators = [
      UniqueTogetherValidator(
          queryset=Mensajero.objects.all(),
          fields=('nombre', 'telefono')
      )
    ]
