from django.urls import path

from .views import list_doctors
from .views import doctor_form_view

urlpatterns = [
    path('', list_doctors),
    path('form/', doctor_form_view)
]
