from rest_framework import serializers

from .models import *


class City_Weather_DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = City_Weather_Data
        
        # Here __all__ serializes all Columns

        # But I listed all for better Understanding.

        fields = '__all__'


