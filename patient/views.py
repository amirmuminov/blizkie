from django.shortcuts import render
from rest_framework.decorators import api_view

from myauth.models import CustomUser
from .models import Meal, Toilet, Mobility, MentalState, LevelSelfServ, City, Place, Patient
from .serializers import MealSerializer, ToiletSerializer, MobilitySerializer, MentalStateSerializer, \
    LevelSelfServSerializer, CitySerializer, PlaceSerializer
from myauth.serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.

class MealView(APIView):
    serializer_class = MealSerializer

    def get(self, request, format=None):
        meals = Meal.objects.all()
        serializer = self.serializer_class(meals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category = Meal(
                name=serializer.validated_data.get('name')
            )
            category.save()

            response_serializer = self.serializer_class(category)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            meal = Meal.objects.get(pk=request.POST.get('id'))
            meal.name = serializer.validated_data.get('name')
            meal.save()

            response_serializer = self.serializer_class(meal)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MealDeleteView(APIView):

    def delete(self, request, pk, format=None):
        Meal.objects.get(pk=pk).delete()
        return Response({"success": "One meal was deleted"}, status=status.HTTP_200_OK)


class ToiletView(APIView):
    serializer_class = ToiletSerializer

    def get(self, request, format=None):
        toilets = Toilet.objects.all()
        serializer = self.serializer_class(toilets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            toilet = Toilet(
                name=serializer.validated_data.get('name')
            )
            toilet.save()

            response_serializer = self.serializer_class(toilet)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            toilet = Toilet.objects.get(pk=request.POST.get('id'))
            toilet.name = serializer.validated_data.get('name')
            toilet.save()

            response_serializer = self.serializer_class(toilet)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ToiletDeleteView(APIView):

    def delete(self, request, pk, format=None):
        Toilet.objects.get(pk=pk).delete()
        return Response({"success": "One toilet was deleted"}, status=status.HTTP_200_OK)


class MobilityView(APIView):
    serializer_class = MobilitySerializer

    def get(self, request, format=None):
        mobilities = Mobility.objects.all()
        serializer = self.serializer_class(mobilities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            mobility = Mobility(
                name=serializer.validated_data.get('name')
            )
            mobility.save()

            response_serializer = self.serializer_class(mobility)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            mobility = Mobility.objects.get(pk=request.POST.get('id'))
            mobility.name = serializer.validated_data.get('name')
            mobility.save()

            response_serializer = self.serializer_class(mobility)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MobilityDeleteView(APIView):

    def delete(self, request, pk, format=None):
        Mobility.objects.get(pk=pk).delete()
        return Response({"success": "One mobility was deleted"}, status=status.HTTP_200_OK)


class MentalStateView(APIView):
    serializer_class = MentalStateSerializer

    def get(self, request, format=None):
        mental_states = MentalState.objects.all()
        serializer = self.serializer_class(mental_states, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            mental_state = MentalState(
                name=serializer.validated_data.get('name')
            )
            mental_state.save()

            response_serializer = self.serializer_class(mental_state)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            mental_state = MentalState.objects.get(pk=request.POST.get('id'))
            mental_state.name = serializer.validated_data.get('name')
            mental_state.save()

            response_serializer = self.serializer_class(mental_state)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MentalStateDeleteView(APIView):

    def delete(self, request, pk, format=None):
        MentalState.objects.get(pk=pk).delete()
        return Response({"success": "One mental state was deleted"}, status=status.HTTP_200_OK)


class LevelSelfServView(APIView):
    serializer_class = LevelSelfServSerializer

    def get(self, request, format=None):
        level_self_serv = LevelSelfServ.objects.all()
        serializer = self.serializer_class(level_self_serv, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            level_self_serv = LevelSelfServ(
                name=serializer.validated_data.get('name')
            )
            level_self_serv.save()

            response_serializer = self.serializer_class(level_self_serv)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            level_self_serv = LevelSelfServ.objects.get(pk=request.POST.get('id'))
            level_self_serv.name = serializer.validated_data.get('name')
            level_self_serv.save()

            response_serializer = self.serializer_class(level_self_serv)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LevelSelfServDeleteView(APIView):

    def delete(self, request, pk, format=None):
        LevelSelfServ.objects.get(pk=pk).delete()
        return Response({"success": "One level self serv state was deleted"}, status=status.HTTP_200_OK)


class CityView(APIView):
    serializer_class = CitySerializer

    def get(self, request, format=None):
        city = City.objects.all()
        serializer = self.serializer_class(city, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            city = City(
                name=serializer.validated_data.get('name')
            )
            city.save()

            response_serializer = self.serializer_class(city)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            city = City.objects.get(pk=request.POST.get('id'))
            city.name = serializer.validated_data.get('name')
            city.save()

            response_serializer = self.serializer_class(city)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CityDeleteView(APIView):

    def delete(self, request, pk, format=None):
        City.objects.get(pk=pk).delete()
        return Response({"success": "One city was deleted"}, status=status.HTTP_200_OK)


class PlaceView(APIView):
    serializer_class = PlaceSerializer

    def get(self, request, format=None):
        place = Place.objects.all()
        serializer = self.serializer_class(place, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            place = Place(
                name=serializer.validated_data.get('name')
            )
            place.save()

            response_serializer = self.serializer_class(place)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            place = Place.objects.get(pk=request.POST.get('id'))
            place.name = serializer.validated_data.get('name')
            place.save()

            response_serializer = self.serializer_class(place)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PlaceDeleteView(APIView):

    def delete(self, request, pk, format=None):
        Place.objects.get(pk=pk).delete()
        return Response({"success": "One place was deleted"}, status=status.HTTP_200_OK)


class PatientView(APIView):
    serializer_class = CustomUserSerializer

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

            patient = Patient(
                user=user,
                lss=LevelSelfServ.objects.get(pk=request.POST.get("lss")),
                ms=MentalState.objects.get(pk=request.POST.get("ms")),
                mobility=Mobility.objects.get(pk=request.POST.get("mobility")),
                toilet=Toilet.objects.get(pk=request.POST.get("toilet")),
                meal=Meal.objects.get(pk=request.POST.get("meal")),
                city=City.objects.get(pk=request.POST.get("city")),
                place=Place.objects.get(pk=request.POST.get("place")),
            )

            patient.save()

            response_serializer = self.serializer_class(user)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)