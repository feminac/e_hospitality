from django.contrib import admin
from .models import Patient, Appointment,MedicalHistory,HealthEducation,Billing


admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalHistory)
admin.site.register(HealthEducation)
admin.site.register(Billing)