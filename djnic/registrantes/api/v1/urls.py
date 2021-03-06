from django.urls import path, include
from rest_framework import routers
from .views import RegistrantViewSet


router = routers.DefaultRouter()
router.register(r'registrante', RegistrantViewSet)

urlpatterns = [
    path('stats/', include('registrantes.api.v1.urls_stats')),
    path('', include(router.urls)),
]
