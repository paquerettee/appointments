from django.shortcuts import render
from rest_framework import viewsets
from .models import Facility, ServiceFacility, Appointment
from .serializers import FacilitySerializer, ServiceFacilitySerializer, AppointmentSerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class ServiceFacilityViewSet(viewsets.ModelViewSet):
    queryset = ServiceFacility.objects.all()
    serializer_class = ServiceFacilitySerializer
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


