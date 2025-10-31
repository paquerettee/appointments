from django.shortcuts import render
from rest_framework import viewsets
from .models import Facility, ServiceFacility, Professional, Client, Appointment
from .serializers import FacilitySerializer, ServiceFacilitySerializer, ProfessionalSerializer, ClientSerializer, AppointmentSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class ServiceFacilityViewSet(viewsets.ModelViewSet):
    queryset = ServiceFacility.objects.all()
    serializer_class = ServiceFacilitySerializer
    
class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


# get rid of it when everything works
    def create(self, request, *args, **kwargs):
        print("Received POST data:", request.data)  # 👈 Add this line
        # return super().create(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation errors:", serializer.errors)  # 👈 This is key
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




