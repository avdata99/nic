from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views
from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework.authtoken import views

from .views import DominioSitemap, RegistranteSitemap, RubroSitemap, HostingSitemap

sitemaps = {
    'dominio': DominioSitemap,
    'registrante': RegistranteSitemap,
    'rubro': RubroSitemap,
    'hosting': HostingSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('djnic.api.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include('web.urls')),
    # Sitemap https://docs.djangoproject.com/en/3.1/ref/contrib/sitemaps/#creating-a-sitemap-index
    path('sitemap.xml', cache_page(86400)(sitemap_views.index), {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', cache_page(86400)(sitemap_views.sitemap), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
