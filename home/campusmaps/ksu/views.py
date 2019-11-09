from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, World!")
    
def floors(request, building_name):
    return HttpResponse("You're looking at the floors for %s Hall" % building_name)

def map(request, building_name, floor_id):
    return HttpResponse("You're looking at the rooms for %s Floor %i" % (building_name, floor_id))