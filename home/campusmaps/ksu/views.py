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
    return HttpResponse("You're looking at the floors for %s Hall" % building_name)

def map(request, building_name, floor_id):
    return HttpResponse("You're looking at the rooms for %s Floor %i" % (building_name, floor_id))