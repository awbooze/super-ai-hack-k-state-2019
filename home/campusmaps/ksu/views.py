from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *

# Index page
def index(request):
    building_list = Building.objects.order_by('name')
    context = {'building_list':building_list}
    return render(request, 'ksu/index.html', context)
    
# List of floors
def floors(request, building_name):
    b = get_object_or_404(Building, name=building_name)
    floor_list = Floor.objects.filter(building = b).order_by('number')
    context = {"floor_list":floor_list, "building_name":building_name}

    return render(request, 'ksu/floors.html', context)

# Map of floor page
def map(request, building_name, floor_id):
    building = get_object_or_404(Building, name=building_name)
    floor = get_object_or_404(Floor, number=floor_id)
    context = {"floor":floor}
    return render(request, 'ksu/map.html', context)

# Search page (same as map page)
def search(request, building_name, room_number):
    room=get_object_or_404(Room, number=room_number)
    floor = room.floor
    context = {"floor":floor}
    return render(request, 'ksu/map.html', context)
