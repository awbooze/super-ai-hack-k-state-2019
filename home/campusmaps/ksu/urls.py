from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:building_name>/', views.floors, name='floors'),
    path('<str:building_name>/<int:floor_id>/', views.map, name='Floor Map')
]