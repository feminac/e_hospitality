from django.urls import path
from . import views
from .views import appointment_list_create, appointment_detail, medical_history_view, health_education_view, \
    billing_view
from .views import appointment_form_view

urlpatterns = [
    path('', views.patient_list_create, name='patient-list-create'),
    path('<int:pk>/', views.patient_detail, name='patient-detail'),
    path('form/', views.patient_form_view, name='patient-form'),
    path('appointments/', appointment_list_create),
    path('appointments/<int:pk>/', appointment_detail),
    path('appointment-form/', appointment_form_view, name='appointment-form'),
    path('medical-history/', medical_history_view, name='medical-history'),
    path('health-education/', health_education_view, name='health-education'),
    path('billing/', billing_view, name='billing'),
]

