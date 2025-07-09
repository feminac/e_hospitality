from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer
from .serializers import DoctorListSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def manage_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        data = [
            {
                "name": doctor.user.first_name,
                "specialty": doctor.specialty
            }
            for doctor in doctors
        ]
        return Response(data)

    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Doctor added'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_doctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorListSerializer(doctors, many=True)
    return Response(serializer.data)



def doctor_form_view(request):
    message = ""
    if request.method == "POST":
        name = request.POST.get('name')
        specialty = request.POST.get('specialty')

        Doctor.objects.create(name=name, specialty=specialty)
        message = "✅ Doctor registered successfully."

    return render(request, "register_doctor.html", {'message': message})