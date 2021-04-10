from django.urls import path 

from . import views

urlpatterns = [
        path('sightings/',views.index),
        path('sightings/detail/',views.detail, name='detail'),
        path('sightings/stats/',views.stats, name='stats'),
        ]

