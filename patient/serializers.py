from rest_framework import serializers
from .models import Meal, Toilet, Mobility, MentalState, LevelSelfServ, City, Place, Patient


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name')


class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = ('id', 'name')


class MobilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobility
        fields = ('id', 'name')


class MentalStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalState
        fields = ('id', 'name')


class LevelSelfServSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelSelfServ
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name')


class PatientSerializer(serializers.ModelSerializer):
    lss = LevelSelfServSerializer(read_only=True)
    ms = MentalStateSerializer(read_only=True)
    mobility = MobilitySerializer(read_only=True)
    toilet = ToiletSerializer(read_only=True)
    meal = MealSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ('lss', 'ms', 'mobility', 'toilet', 'meal', 'city', 'place')