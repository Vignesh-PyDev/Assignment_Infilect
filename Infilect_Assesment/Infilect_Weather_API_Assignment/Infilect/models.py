from django.db import models

# Create your models here.

from .models import *


class City_Weather_Data(models.Model):
    city_name = models.CharField(max_length=15)
    city_weather_condn = models.CharField(max_length=30)
    city_time = models.CharField(max_length=15)
    city_date = models.CharField(max_length=15)

    def __str__(self):
        return "%s - %s" % (self.group, self.user)

class City_Names(models.Model):
    city_name = models.CharField(max_length=15)
    
    # def __str__(self):
    #     return "%s - %s" % (self.group, self.user)

