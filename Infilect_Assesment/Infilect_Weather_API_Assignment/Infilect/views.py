from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK)
from rest_framework.response import Response

from .models import *

from .serializers import City_Weather_DataSerializer

import json

import os

import requests

import random

from rest_framework.pagination import PageNumberPagination

from django.core import serializers



@csrf_exempt

@api_view(["POST"])

@permission_classes((AllowAny,))

def login(request):
	username = request.data.get("username")
	password = request.data.get("password")
	if username is None or password is None:
		return Response({'error': 'Please Enter Both Username and Passwords'},
						status=HTTP_400_BAD_REQUEST)
	user = authenticate(username = username, password = password)
	if not user:
		return Response({'error': 'Invalid Credentials'},
						status=HTTP_404_NOT_FOUND)
	token, _ = Token.objects.get_or_create(user=user)
	return Response({'token': token.key},
					status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def weatherapi(request):

	# Here city names json file is fetched from openweathermap.org 

	City_List = json.load(open(os.getcwd() + "/Infilect" +'/city_names.json'))

	City_Names = [City['city']['name'] for City in City_List]

	# Here why I used 120 is in that json file i got around 3k cities names but weatherapi.com gives weather information only for feweer cities so I used 120.

	# if i used exact 30 i get weather info only for about 10-12.

	City_Names_Final = [City_Names[random.randint(0,len(City_Names))] for x in range(120)]

	# To restrict weather info only for 35 cities.

	Max_No = 0

	try:


		for i in City_Names_Final:

			# Here according to Assignment i have to use https://openweathermap.org/api but its asks card details for api usage even for free plan

			# so i found an alternate which is free till 27-SEP-2022.

			Loop_var = requests.get(r'http://api.weatherapi.com/v1/current.json?key=e69637d6112d404ba5960930221309&q='+i+'&aqi=no').json()

			Weather_Data = City_Weather_Data(

				city_name = i,
				city_weather_condn = Loop_var['current']['condition']['text'],
				city_time = Loop_var['current']["last_updated"][-5:],
				city_date = Loop_var['current']['last_updated'][:-5]
			
				)


			Weather_Data.save()

			Max_No += 1

			# here 35 used to restrict loop

			if Max_No >35:break

			# Here why I used 35 every time i call that api the new data in inserted 

			# i checked with inspectdb its around 100+ rows inserted so i used 35 as given in Requirement.

			# values() method used to convert queryset into json

			all_data = City_Weather_Data.objects.all().values()[0:35]

		
	except:

		pass

	page = PageNumberPagination()

	# 10 as given in requirement

	page.page_size = 10

	query = all_data

	context = page.paginate_queryset(query,request)

	# Here in serializers we specified all in fields in fileds if we give exact columns it fetches only those columns.

	serializer = City_Weather_DataSerializer(context,many=True)

	return page.get_paginated_response(serializer.data)

@csrf_exempt

@api_view(["POST"])

@permission_classes((AllowAny,))

def logout(request):
	
	if request.user.auth_token:

		print(request)

		request.user.auth_token.delete()

		return Response('User Logged out successfully')    


