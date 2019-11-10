from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newBuilding/', views.newBuilding, name='newBuilding'),
    path('search/<str:building_name>/<int:room_number>/', views.search, name='search'),
    path('<str:building_name>/<int:floor_id>/', views.map, name='map'),
    path('<str:building_name>/', views.floors, name='floors')
    

]