from rest_framework import serializers
from .models import Cars, Logs


class Carserializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('unit', 'manufacturer', 'status', 'mileage')


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ('unit', 'log_date', 'new_mileage')
