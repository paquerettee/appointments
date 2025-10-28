from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.booking.views import FacilityViewSet, ServiceFacilityViewSet, AppointmentViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet)
router.register('facilities', FacilityViewSet)
router.register('service-facility', ServiceFacilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]