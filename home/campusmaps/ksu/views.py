from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.

def index(request):
    building_list = Building.objects.order_by('-name')
    context = {'building_list':building_list}
    return render(request, 'ksu/index.html', context)
    
def floors(request, building_name):
    b= get_object_or_404(Building, name=building_name)
    floors_list = Floor.objects.filter(building = b).order_by('number')
    context = {"floors_list":floors_list}
    return render(request, 'ksu/floors.html', context)

def map(request, building_name, floor_id):
    return HttpResponse("You're looking at the rooms for %s Floor %i" % (building_name, floor_id))
#def search(request, building_name, room_number):
