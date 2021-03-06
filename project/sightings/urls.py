from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('stats/', views.stats, name='stats'),
	path('sightings/', views.data_show, name='sightings'),
    path('map/', views.show_map, name='map'),
    path('<squirrel_id>/', views.detail, name='detail'),
    
    
]
