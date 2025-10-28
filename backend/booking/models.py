from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Professional(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    services = models.ManyToManyField(Service, through='ServiceFacility')
    def __str__(self):
        return self.name

class ProfessionalService(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('professional', 'service')

    def __str__(self):
        return f"{self.professional} – {self.service}"

class ProfessionalFacility(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('professional', 'facility')

    def __str__(self):
        return f"{self.professional} @ {self.facility}"

class ServiceFacility(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('service', 'facility')
    def __str__(self):
        return f"{self.service} @ {self.facility}"


class AppointmentStatus(models.TextChoices):
    SCHEDULED = 'scheduled', 'Scheduled'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'
    NO_SHOW = 'no_show', 'No-show'

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    date = models.DateTimeField()
    date_established = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.SCHEDULED
    )

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M')} – {self.client} z {self.professional} ({self.status})"




