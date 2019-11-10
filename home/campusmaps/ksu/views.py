from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import UploadSVG
from django.core.files.storage import FileSystemStorage
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
    floor = get_object_or_404(Floor, number=floor_id, building = building)
    context = {"floor":floor}
    return render(request, 'ksu/map.html', context)

# Search page (same as map page)
def search(request, building_name, room_number):
    room=get_object_or_404(Room, number=room_number)
    floor = room.floor
    context = {"floor":floor}
    return render(request, 'ksu/map.html', context)

def newBuilding(request):
    if request.method == 'POST':
        form = UploadSVG(request.POST, request.FILES)
        if form.is_valid():
            if not Building.objects.filter(name=form.cleaned_data["building_name"]).exists():
                b=Building(name=form.cleaned_data["building_name"], abbreviation=form.cleaned_data["abbreviation"])
                b.save()
            b = Building.objects.get(name = form.cleaned_data["building_name"])
            if not Floor.objects.filter(building=b, number=form.cleaned_data["floorNum"]).exists():
                f=Floor(building=b,number=form.cleaned_data["floorNum"])
                f.save()
                url = handle_uploaded_file(request.FILES['image'], b.name, f.number)
                return HttpResponse(url)
            return HttpResponse("Thanks!")
    else:
        form = UploadSVG()
    return render(request, 'ksu/newBuilding.html', {'form':form})

def handle_uploaded_file(f, b, n):
    fs = FileSystemStorage()
    filename = fs.save("svg/"+b+"_"+n.__str__()+".svg", f)
    return fs.url("svg/"+b+"_"+n.__str__()+".svg")
