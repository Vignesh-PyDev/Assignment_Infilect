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

	all_data = City_Weather_Data.objects.all().values()[0:30]

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


