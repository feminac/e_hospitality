from django.db import models
from doctors.models import Doctor
class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
class Appointment(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_contact = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient_name} with {self.doctor.name} on {self.date}"

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_history')
    diagnosis = models.TextField()
    medications = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"History of {self.patient.name} on {self.date_recorded}"



class HealthEducation(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Billing(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')])
    payment_date = models.DateField(null=True, blank=True)
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Bill for {self.patient.name} - ₹{self.amount}"
