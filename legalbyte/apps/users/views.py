from django.shortcuts import render
from rest_framework import generics
from apps.users.serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer