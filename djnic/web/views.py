from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, cache_control
from django.views.generic.base import TemplateView
from django.views.generic import FormView

from web.forms import SearchForm
from cambios.data import get_ultimos_caidos, get_ultimas_transferencias
from dominios.data import get_ultimos_registrados
from dnss.data import get_hosting_usados
from core.data import get_search_results

from core.views import AnalyticsViewMixin
from dominios.models import Dominio
from registrantes.models import Registrante
from dnss.models import Empresa, DNS


class HomeView(AnalyticsViewMixin, TemplateView):

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


class TermsView(AnalyticsViewMixin, TemplateView):

    template_name = "web/bootstrap-base/terms_of_service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Términos y condiciones'
        context['site_description'] = 'Términos y condiciones de la app DominiosAR'

        return context


class PrivaciPolicyView(AnalyticsViewMixin, TemplateView):

    template_name = "web/bootstrap-base/privacy_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Política de privacidad'
        context['site_description'] = 'Política de privacidad de la app DominiosAR'

        return context


class AboutView(AnalyticsViewMixin, TemplateView):

    template_name = "web/bootstrap-base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Acerca de Dominios Argentinos'
        context['site_description'] = 'Dominios Argentinos es un proyecto de OpenDataCordoba'

        return context


class SearchResultsView(AnalyticsViewMixin, FormView):

    form_class = SearchForm
    template_name = "web/bootstrap-base/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Acerca de Dominios Argentinos'
        context['site_description'] = 'Dominios Argentinos es un proyecto de OpenDataCordoba'

        query = self.request.GET.get('query')
        context['query'] = query

        context.update(get_search_results(query))

        return context


class LoginView(TemplateView):

    template_name = "web/bootstrap-base/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Login'
        context['site_description'] = 'Registrarse o acceder a DominiosAR'

        return context
