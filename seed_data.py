from appointments.models import Client, Professional, Service, Location, Appointment, AppointmentStatus
from datetime import datetime, timedelta

def run():
    # Clients
    clients = [
        Client.objects.create(name="Alice Johnson", email="alice@example.com"),
        Client.objects.create(name="Bob Smith", email="bob@example.com"),
        Client.objects.create(name="Catherine Lee", email="catherine@example.com"),
        Client.objects.create(name="David Brown", email="david@example.com"),
        Client.objects.create(name="Eva Green", email="eva@example.com"),
    ]

    # Professionals
    professionals = [
        Professional.objects.create(name="Dr. Emily Carter", specialty="Dermatology"),
        Professional.objects.create(name="Dr. Michael Stone", specialty="Physiotherapy"),
        Professional.objects.create(name="Dr. Olivia White", specialty="Psychology"),
    ]

    # Services
    services = [
        Service.objects.create(name="Skin Consultation", duration=timedelta(minutes=30)),
        Service.objects.create(name="Deep Tissue Massage", duration=timedelta(minutes=60)),
        Service.objects.create(name="Therapy Session", duration=timedelta(minutes=45)),
    ]

    # Locations
    locations = [
        Location.objects.create(name="Downtown Clinic", address="123 Main St, Cityville"),
        Location.objects.create(name="Uptown Wellness Center", address="456 Elm St, Cityville"),
    ]

    # Appointments
    base_date = datetime(2025, 11, 3, 9, 0)
    for i in range(12):
        Appointment.objects.create(
            client=clients[i % len(clients)],
            professional=professionals[i % len(professionals)],
            service=services[i % len(services)],
            location=locations[i % len(locations)],
            date=base_date + timedelta(hours=i),
            status=AppointmentStatus.SCHEDULED if i % 4 != 0 else AppointmentStatus.COMPLETED
        )