from rest_framework import serializers
from .models import Sitter, Day


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'name')


class SitterSerializer(serializers.ModelSerializer):
    working_days = DaySerializer(read_only=True, many=True)

    class Meta:
        model = Sitter
        fields = ('date_of_birth', 'payment', 'experience', 'working_days')
