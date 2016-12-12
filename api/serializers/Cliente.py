# pylint: disable=W0311, C0111
from rest_framework import serializers
from core.models import Cliente
from .PhoneNumber import PhoneNumberSerializer

class ClienteSerializerGET(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = '__all__'


class ClienteSerializerPATCH(serializers.ModelSerializer):
  nombre = serializers.CharField(required=False)
  email = serializers.EmailField(required=False)
  telefono = PhoneNumberSerializer(required=False)
  class Meta:
    model = Cliente
    exclude = ('id',)

class ClienteSerializerNEW(serializers.ModelSerializer):
  nombre = serializers.CharField(required=True)
  email = serializers.EmailField(required=True)
  telefono = PhoneNumberSerializer(required=True)
  class Meta:
    model = Cliente
    fields = '__all__'
