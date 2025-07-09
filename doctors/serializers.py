from rest_framework import serializers
from .models import Doctor

# Serializer for creating and updating doctors
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','name', 'specialty']

# Serializer for listing doctors (optional: same as above)
class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','name', 'specialty']
