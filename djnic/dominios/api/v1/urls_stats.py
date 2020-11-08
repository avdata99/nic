from django.urls import path, include
from rest_framework import routers
from .views_stats import GeneralStatsView, PriorityView, ReadingStatsView


urlpatterns = [
    path('general', GeneralStatsView.as_view()),
    path('priority', PriorityView.as_view()),
    path('reading', ReadingStatsView.as_view()),
    path('reading/<int:desde_dias>', ReadingStatsView.as_view()),
    path('reading/<int:desde_dias>/<int:hasta_dias>', ReadingStatsView.as_view()),
    

]
