from rest_framework import serializers
from .models import CustomUser
from sitter.serializers import SitterSerializer
from patient.serializers import PatientSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    child_sitter = SitterSerializer(read_only=True)
    child_patient = PatientSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_sitter', 'is_patient', 'child_sitter',
                  'child_patient')



