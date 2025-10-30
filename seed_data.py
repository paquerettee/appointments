from backend.booking.models import (
    Client, Professional, Service, Facility, ServiceFacility,
    Appointment, AppointmentStatus
)
from datetime import datetime, timedelta
from django.utils import timezone

def run():
    # Clients
    clients = [
        Client.objects.create(
            first_name="Alice", last_name="Johnson",
            email="alice@example.com", phone="123456789"
        ),
        Client.objects.create(
            first_name="Bob", last_name="Smith",
            email="bob@example.com", phone="987654321"
        ),
        Client.objects.create(
            first_name="Catherine", last_name="Lee",
            email="catherine@example.com", phone="555123456"
        ),
        Client.objects.create(
            first_name="David", last_name="Brown",
            email="david@example.com", phone="444987654"
        ),
        Client.objects.create(
            first_name="Eva", last_name="Green",
            email="eva@example.com", phone="333222111"
        ),
    ]

    # Professionals
    professionals = [
        Professional.objects.create(first_name="Emily", last_name="Carter"),
        Professional.objects.create(first_name="Michael", last_name="Stone"),
        Professional.objects.create(first_name="Olivia", last_name="White"),
    ]

    # Services
    services = [
        Service.objects.create(name="Skin Consultation", duration=timedelta(minutes=30), price=50.00),
        Service.objects.create(name="Deep Tissue Massage", duration=timedelta(minutes=60), price=80.00),
        Service.objects.create(name="Therapy Session", duration=timedelta(minutes=45), price=70.00),
    ]

    # Facilities
    facilities = [
        Facility.objects.create(
            name="Downtown Clinic", address="123 Main St, Cityville",
            phone="111222333", email="downtown@example.com", main_img="facilities/GPTImage_001.png"

        ),
        Facility.objects.create(
            name="Uptown Wellness Center", address="456 Elm St, Cityville",
            phone="444555666", email="uptown@example.com", main_img="facilities/GPTImage_002.png"
        ),
    ]

    # Linking service and facility
    service_facility = [
        ServiceFacility.objects.create(facility=facilities[0], service=services[0]),
        ServiceFacility.objects.create(facility=facilities[0], service=services[1]),
        ServiceFacility.objects.create(facility=facilities[1], service=services[1]),
        ServiceFacility.objects.create(facility=facilities[1], service=services[2]),
    ]

    # Appointments
    base_date = timezone.make_aware(datetime(2025, 11, 3, 9, 0))
    for i in range(12):
        Appointment.objects.create(
            client=clients[i % len(clients)],
            professional=professionals[i % len(professionals)],
            service=services[i % len(services)],
            facility=facilities[i % len(facilities)],
            date=base_date + timedelta(hours=i),
            status=AppointmentStatus.SCHEDULED if i % 4 != 0 else AppointmentStatus.COMPLETED
        )

def delete_all_data():
    Client.objects.all().delete()
    Professional.objects.all().delete()
    Service.objects.all().delete()
    Facility.objects.all().delete()
    Appointment.objects.all().delete()
    ServiceFacility.objects.all().delete()