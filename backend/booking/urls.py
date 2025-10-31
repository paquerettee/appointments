from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.booking.views import FacilityViewSet, ServiceFacilityViewSet, ProfessionalViewSet, AppointmentViewSet, ClientViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet)
router.register('facilities', FacilityViewSet)
router.register('professional', ProfessionalViewSet)
router.register('service-facility', ServiceFacilityViewSet)
router.register('clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]