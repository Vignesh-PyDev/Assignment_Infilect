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

            

            # Here according to Assignment i have to use https://openweathermap.org/api but its asks card details for api usage even for free plan

            # so i found an alternate which is free till 27-SEP-2022.

            # print("http://api.weatherapi.com/v1/current.json?key=8f88c80af0744fff9b631859221509&q='+x['city_name']+'&aqi=no")

            Loop_var = requests.get(r'http://api.weatherapi.com/v1/current.json?key=8f88c80af0744fff9b631859221509&q='+x['city_name']+'&aqi=no').json()

            # print(Loop_var,"skjfhsdkjfh")

            

            Weather_Data = City_Weather_Data(

                city_name = x['city_name'],
                city_weather_condn = Loop_var['current']['condition']['text'],
                city_time = Loop_var['current']["last_updated"][-5:],
                city_date = Loop_var['current']['last_updated'][:-5]
            
                )


            Weather_Data.save()

            

            # Max_No += 1

            # here 35 used to restrict loop

            # if Max_No >35:break

            # Here why I used 35 every time i call that api the new data in inserted 

            # i checked with inspectdb its around 100+ rows inserted so i used 35 as given in Requirement.

            # values() method used to convert queryset into json

            

            
    except:

        pass

    return 0


Brownie_Point_1()

# print(City_Weather_Data.objects.all())       

# # print("Geeksforgeeks")

schedule.every(10).minutes.do(Brownie_Point_1)

while True:
    schedule.run_pending()
    time.sleep(1)