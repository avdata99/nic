from datetime import timedelta
import json
import logging
import random
from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache, cache_control
from rest_framework import filters
from rest_framework.decorators import action
from .serializer import FullCambiosDominioSerializer, FullCampoCambioSerializer
from cambios.models import CambiosDominio, CampoCambio


logger = logging.getLogger(__name__)


@method_decorator(cache_control(max_age=settings.GENERAL_CACHE_SECONDS), name='dispatch')
@method_decorator(cache_page(settings.GENERAL_CACHE_SECONDS), name='dispatch')
class CambiosDominioViewSet(viewsets.ModelViewSet):
    queryset = CambiosDominio.objects.all()
    serializer_class = FullCambiosDominioSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['-id']


@method_decorator(cache_control(max_age=settings.GENERAL_CACHE_SECONDS), name='dispatch')
@method_decorator(cache_page(settings.GENERAL_CACHE_SECONDS), name='dispatch')
class CampoCambioViewSet(viewsets.ModelViewSet):
    queryset = CampoCambio.objects.all()
    serializer_class = FullCampoCambioSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['campo', 'anterior', 'nuevo']
    ordering_fields = '__all__'
    ordering = ['-id']
