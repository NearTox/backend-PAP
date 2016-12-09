# pylint: disable=W0311, C0111
from rest_framework import serializers
from core.models import DatosPostales
class DatosPostalesSerializer(serializers.ModelSerializer):
  class Meta:
    model = DatosPostales
    fields = '__all__'
