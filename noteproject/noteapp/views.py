from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from noteapp.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from django.core.paginator import Paginator



class NoteView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]


    def get(self,request):
        try:
            notes=Note.objects.all()

            if request.GET.get("search"):
                search=request.GET.get("search")
                notes=Note.objects.filter(Q(title__icontains=title)|Q(contents__icontains=content))
            page_number=request.GET.get('page',1)
            paginator=Paginator(notes,1)
            serializer=Noteserializer(paginator.page(page_number),many=True)

            return Response({"data":serializer.data,"message":"this is not allowed"})
            
        except Exception as e:
            print(e)
            return Response({"data":{},"message":"something went wrong...!"})

    def post(self,request):
        try:
            data=request.data
            data['user']=request.user.id
            serializer=Noteserializer(data=data)
            print(serializer)

            if not serializer.is_valid():
                return Response({"data":serializer.errors,"message":"something went wrong..!"})


            serializer.save()

            return Response({"data":serializer.data,"message":"Note Created...!"})

        except Exception as e:
            print(e)
            return Response({"data":{},"message":"something went error..!"})


    def patch(self,request):
        try:
            data=request.data
            blog=Blog.objects.filter(uid=data.get("uid"))

            if not blog.exist():
                return {"message":"Invalid Blog..","data":{} }

            if  request.user!= user.blog[0] :
                return {"data":{},"message":"your are not authorised to do this..."}


            serilaizer=Noteserializer(blog[0],data=data,partial=True)
            if not  serializer.is_valid():
                return Response({"data":serilaizer.errors,"message":"It's not Working...!"})


            serilaizer.save()

            return Response({"data":serilaizer.data,"message":"Blog Edited Successfully..!"})

        except Exception as e:
            print(e)
            return Response({"data":serilaizer.errors,"message":"something went wrong.."})



    def delete(self,request):
        try:
            data=request.data
            blog=Blog.objects.filter(uid=data.get("uid"))

            if not blog.exist():
                return({"data":{},"message":"The blog not exist..!"})

            if request.user!= user.blog[0]:
                return({"data":{},"message":"The user doesn't exist"})


            blog[0].delete
            return({"data":{},"message":"the Note is deleted...!"})

        except Exception as e:
            print(e)
            return({"data":{},"message":"The user doesn't exist"})


