from rest_framework import serializers
from .models import Facility, Service, ServiceFacility, Professional, Client, Appointment

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'duration']

class FacilitySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Facility
        fields = '__all__'
        # fields = ['id', 'name', 'address', 'email', 'phone', 'main_img', 'services']

class ServiceFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFacility
        fields = '__all__'

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'