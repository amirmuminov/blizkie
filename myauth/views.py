from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from .models import CustomUser


# Create your views here.

class CustomUserView(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)
