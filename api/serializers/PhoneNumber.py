# pylint: disable=W0311, C0111
from rest_framework import serializers
from phonenumber_field.validators import validate_international_phonenumber

class PhoneNumberSerializer(serializers.CharField):
  validators = [validate_international_phonenumber]
