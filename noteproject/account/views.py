from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from account.serializers import *
from rest_framework.response import Response


class RegisterView(APIView):
	def post(self,request):
		try:
			data = request.data
			serializer = RegisterSerializer(data=data)

			if not serializer.is_valid():
				return Response({
					'data': serializer.errors,
					'message':'something went wrong'
					})

			serializer.save()

			return Response({
				  'data':{},
				  'message':'your account is created'
				  })
		except Exception as e:
			return Response({
				  'data':{},
				  'message':'something wrong'
				})

	# def post(self,request):
	# 	try:
	# 		data=request.data
	# 		serializer=RegisterSerializer(data=data)
	# 		if not serializer.is_valid():
	# 			return Response({"data":serializer.errors,"message":"something went wrongs..!"})

	# 		serializer.save()

	# 		return Response({"data":{},
	# 			"message":"Your Account is Created Successfully..!"

	# 			})

	# 	except Exception as e:
	# 		print(e)
	# 		return Response({"data":data,
	# 			"message":"something went wrong...!"})


class LoginView(APIView):
	def post(self,request):
		try:
			data= request.data
			serializer=LoginSerializer(data=data)

			if not serializer.is_valid():
				return Response({"data":serializer.errors,"message":"something went wrong..!"})

			response=serializer.get_jwt_token(serializer.data)

			return Response(response)

		except Exception as e:
			print(e)
			return Response({"data":{},"message":"Something Went Wrong...!"})



		

