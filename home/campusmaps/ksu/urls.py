from django.urls import path, re_path

from . import views
app_name='ksu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:building_name>/<int:floor_id>/', views.map, name='map'),
    path('<str:building_name>/', views.floors, name='floors')
]