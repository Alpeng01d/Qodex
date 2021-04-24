#PACKAGE IMPORT
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
#LOCAL IMPORT
from core.serializers import UserSerializer, Weight_typesSerializer, OperatorsSerializer, Qodex_achiveSerializer, Cm_events_logSerializer
from core.models import Weight_types, Operators, Qodex_achive, Cm_events_log

#API

class Login(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Weight_typesViews(generics.ListCreateAPIView):
    queryset = Weight_types.objects.all()
    serializer_class = Weight_typesSerializer

class OperatorsViews(generics.ListCreateAPIView):
    queryset = Operators.objects.all()
    serializer_class = OperatorsSerializer    

class Qodex_achiveViews(generics.ListCreateAPIView):
    queryset = Qodex_achive.objects.all()
    serializer_class = Qodex_achiveSerializer   
    
class Cm_events_logViews(generics.ListCreateAPIView):
    queryset = Cm_events_log.objects.all()
    serializer_class = Cm_events_logSerializer  