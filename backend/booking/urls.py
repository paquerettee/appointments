from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.booking.views import AppointmentViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]