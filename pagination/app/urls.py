from django.urls import path
import urllib

from app.views import index, bus_stations


urlpatterns = [
    path('', index, name='index'),
    path('bus_stations/', bus_stations, name='bus_stations'),
]
