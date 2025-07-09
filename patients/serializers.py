from rest_framework import serializers
from .models import Patient
from .models import Appointment

from .models import MedicalHistory
from .models import HealthEducation
from.models import Billing
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'



class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)  # 👈 add this

    class Meta:
        model = Appointment
        fields = ['id', 'patient_name', 'patient_contact', 'doctor', 'doctor_name', 'date', 'time', 'reason']


class MedicalHistorySerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = MedicalHistory
        fields = ['id', 'patient', 'patient_name', 'diagnosis', 'medications', 'allergies', 'treatment']

class HealthEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthEducation
        fields = '__all__'


class BillingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = Billing
        fields = ['id', 'patient', 'patient_name', 'amount', 'payment_status', 'payment_date', 'insurance_provider']