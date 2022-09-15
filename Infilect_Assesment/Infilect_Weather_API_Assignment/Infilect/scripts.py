import time
import sqlite3

import json

import random

import requests

import schedule

from Infilect.models  import *


print("ss")

def Brownie_Point_1():

    City_Weather_Data.objects.all().delete()

    try:

        
        for x in City_Names.objects.all().values():

            
            Loop_var = requests.get(r'http://api.weatherapi.com/v1/current.json?key=8f88c80af0744fff9b631859221509&q='+x['city_name']+'&aqi=no').json()

            
            Weather_Data = City_Weather_Data(

                city_name = x['city_name'],
                city_weather_condn = Loop_var['current']['condition']['text'],
                city_time = Loop_var['current']["last_updated"][-5:],
                city_date = Loop_var['current']['last_updated'][:-5]
            
                )


            Weather_Data.save()
            
    except:

        pass

Brownie_Point_1()

schedule.every(10).minutes.do(Brownie_Point_1)

while True:
    schedule.run_pending()
    time.sleep(1)