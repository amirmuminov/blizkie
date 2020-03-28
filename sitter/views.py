from django.contrib.auth.base_user import BaseUserManager
from django.shortcuts import render
from django.utils import timezone

from .models import Day, Sitter
from .serializers import DaySerializer, SitterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myauth.models import CustomUser
from myauth.serializers import CustomUserSerializer


# Create your views here.

class SitterViews(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request, format=None):
        sitter = Sitter.objects.all().prefetch_related('working_days')
        serializer = self.serializer_class(sitter, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(
                username=serializer.validated_data.get("username"),
                password=serializer.validated_data.get("password"),
                first_name=serializer.validated_data.get("first_name"),
                last_name=serializer.validated_data.get("last_name"),
                is_sitter=serializer.validated_data.get("is_sitter"),
                is_patient=serializer.validated_data.get("is_patient"),
                email=serializer.validated_data.get("email")
            )
            user.save()

            sitter = Sitter(
                user=user,
                experience=request.POST.get("experience"),
                date_of_birth=request.POST.get("date_of_birth"),
                payment=request.POST.get("payment")
            )
            sitter.save()
            working_days = Day.objects.filter(pk__in=request.POST.getlist("working_days"))
            for day in working_days:
                sitter.working_days.add(day)

            response_serializer = self.serializer_class(user)
            return Response(response_serializer.data)

        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            sitter = Sitter.objects.get(pk=request.POST["id"])
            sitter.login = serializer.validated_data.get("login")
            sitter.password = serializer.validated_data.get("password")
            sitter.name = serializer.validated_data.get("name")
            sitter.data_of_birth = serializer.validated_data.get("data_of_birth")
            sitter.payment = serializer.validated_data.get("payment")

            sitter.save()
            sitter.working_days.clear()
            working_days = Day.objects.filter(pk__in=request.POST.getlist("working_days"))
            for day in working_days:
                sitter.working_days.add(day)

            response_serializer = self.serializer_class(sitter)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SitterDeleteView(APIView):

    def delete(self, request, pk, format=None):
        Sitter.objects.get(pk=pk).delete()
        return Response({"success": " one sitter is deleted"}, status=200)


