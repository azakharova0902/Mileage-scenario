import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Cars, Logs
from .serializers import Carserializer, LogsSerializer
# Create your views here.

class CarsView(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = Carserializer


class LogsView(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer

