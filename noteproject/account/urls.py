from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework.views import APIView
from account.views import RegisterView,LoginView

urlpatterns = [
path('register/',RegisterView.as_view()),
path('login/',LoginView.as_view()),
]