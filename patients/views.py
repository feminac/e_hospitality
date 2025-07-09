from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, MedicalHistory, HealthEducation, Billing
from .serializers import PatientSerializer, MedicalHistorySerializer, HealthEducationSerializer, BillingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializers import AppointmentSerializer
from doctors.models import Doctor
# API View for JSON-based CRUD
@api_view(['GET', 'POST'])
def patient_list_create(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response({'message': 'Patient deleted'}, status=status.HTTP_204_NO_CONTENT)


# Form-based registration
def patient_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        Patient.objects.create(name=name, age=age, gender=gender, contact=contact, address=address)
        return render(request, 'patients/patient_form.html', {'message': '✅ Patient registered successfully!'})

    return render(request, 'patients/patient_form.html')



@api_view(['GET', 'POST'])
def appointment_list_create(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        appointment.delete()
        return Response({'message': 'Deleted'}, status=204)




def appointment_form_view(request):
    doctors = Doctor.objects.all()  # ✅ Get list of all doctors

    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        patient_contact = request.POST['patient_contact']
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        reason = request.POST['reason']

        doctor = Doctor.objects.get(id=doctor_id)
        Appointment.objects.create(
            patient_name=patient_name,
            patient_contact=patient_contact,
            doctor=doctor,
            date=date,
            time=time,
            reason=reason
        )
        return redirect('/api/patients/appointment-form/')

    return render(request, 'appointment_form.html', {'doctors': doctors})




@api_view(['GET', 'POST'])
def medical_history_view(request):
    if request.accepted_renderer.format == 'html' or not request.META.get('HTTP_ACCEPT', '').startswith('application/json'):
        if request.method == 'POST':
            name = request.POST.get('patient_name')
            diagnoses = request.POST.get('diagnoses')
            medications = request.POST.get('medications')
            allergies = request.POST.get('allergies')
            treatment = request.POST.get('treatment_history')

            if name and diagnoses:
                MedicalHistory.objects.create(
                    patient_name=name,
                    diagnoses=diagnoses,
                    medications=medications,
                    allergies=allergies,
                    treatment_history=treatment
                )
                return redirect('medical-history')

        histories = MedicalHistory.objects.all()
        return render(request, 'medical_history.html', {'histories': histories})

    if request.method == 'GET':
        histories = MedicalHistory.objects.all()
        serializer = MedicalHistorySerializer(histories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MedicalHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Medical history added successfully'})
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def health_education_view(request):
    if request.method == 'GET':
        resources = HealthEducation.objects.all()
        serializer = HealthEducationSerializer(resources, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HealthEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Resource added successfully'})
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def billing_view(request):
    if request.method == 'GET':
        bills = Billing.objects.all()
        serializer = BillingSerializer(bills, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BillingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Billing record added'})
        return Response(serializer.errors, status=400)