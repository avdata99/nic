from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, cache_control
from django.views.generic.base import TemplateView

from cambios.data import get_ultimos_caidos, get_ultimas_transferencias
from dominios.data import get_ultimos_registrados
from dnss.data import get_hosting_usados


@method_decorator(cache_control(max_age=settings.GENERAL_CACHE_SECONDS), name='dispatch')
@method_decorator(cache_page(settings.GENERAL_CACHE_SECONDS), name='dispatch')
class HomeView(TemplateView):

    template_name = "web/bootstrap-base/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'NIC Data'
        context['site_description'] = 'Sitio con información de registros de dominios argentinos'

        context['ultimos_caidos'] = get_ultimos_caidos(limit=5)
        context['ultimos_registrados'] = get_ultimos_registrados(limit=5)
        context['hostings'] = get_hosting_usados(days_ago=0, limit=5)
        context['hostings_last_30_days'] = get_hosting_usados(days_ago=30, limit=5)
        context['news_from_tags'] = get_ultimos_registrados(limit=5, de_registrantes_etiquetados=True)
        context['transferencias'] = get_ultimas_transferencias(limit=5)

        return context


@method_decorator(cache_control(max_age=settings.GENERAL_CACHE_SECONDS), name='dispatch')
@method_decorator(cache_page(settings.GENERAL_CACHE_SECONDS), name='dispatch')
class AboutView(TemplateView):

    template_name = "web/bootstrap-base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Acerca de Dominios Argentinos'
        context['site_description'] = 'Dominios Argentinos es un proyecto de OpenDataCordoba'

        return context
