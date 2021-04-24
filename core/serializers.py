#PACKAGE IMPORTS
from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms import HiddenInput

#LOCAL IMPORTS
from core.models import Weight_types, Operators, Qodex_achive, Cm_events_log


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for auth API """
    class Meta:
        model = User
        fields = ("__all__")

class Weight_typesSerializer(serializers.ModelSerializer):
    """ Serializer for auth API """
    class Meta:
        model = Weight_types
        fields = ("__all__")

class OperatorsSerializer(serializers.ModelSerializer):
    """ Serializer for auth API """
    class Meta:
        model = Operators
        fields = ("__all__")

class Qodex_achiveSerializer(serializers.ModelSerializer):
    """ Serializer for auth API """
    class Meta:
        model = Qodex_achive
        fields = ("__all__")

class Cm_events_logSerializer(serializers.ModelSerializer):
    """ Serializer for auth API """
    class Meta:
        model = Cm_events_log
        fields = ("__all__")
        