from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from osgeo import gdal
import json

from django.core.management.base import BaseCommand
import pandas as pd
from .models import *
from shapely.geometry import Point, Polygon


def home(request):
    return render(request, 'welcome.html')



    
def draw_area_on_map(request):
    # Define the polygon vertices as a list of tuples (latitude, longitude)
    polygon_vertices = [(37.774956, -122.442481), 
                        (37.774956, -122.428481), 
                        (37.758956, -122.428481),
                        (37.758956, -122.442481)]

    # Pass the polygon vertices to the template context
    context = {'polygon_vertices': polygon_vertices}
    
    if request.method=="POST":
        uname = request.POST.get('vertices')
        zonename = request.POST.get('zonename')
        print(uname)
        print(type(uname))
        map_zone = MapZone(name=zonename, Polygon=uname)
        map_zone.save()
        return redirect('admin:app1_mapzone_changelist')

    # Render the template with the Google Map
    return render(request, 'map.html', context)

# for fiend location is in zone or not


def check_zone(request):
    if request.method=="POST":
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        datas = MapZone.objects.all()
        for data in datas:
            # Split the coordinates string into individual pairs of latitude and longitude
            pairs = (data.Polygon).split(",")
            # Convert each pair of coordinates into a tuple of floats
            data_list = [(float(pair.split()[0]), float(pair.split()[1])) for pair in pairs]
            zone = Polygon(data_list)
            def in_zone(lat, lon):
                location = Point(lat, lon)
                return zone.contains(location)
            if in_zone(lat,lon)==True:
                return HttpResponse(f"the locations is inside the zone {data.name}")
            else:
                pass
    return render(request, 'find.html',)

def showzone(request,id):
    lat_lng_str = MapZone.objects.get(id=id)
    coords = (lat_lng_str.Polygon).split(',')
    zone_data = [{'lat': float(coord.split()[0]), 'lng': float(coord.split()[1])} for coord in coords]
    context = {'zone_data': zone_data}
    return render(request, 'my_template.html', context)



def testing(request):
    template = loader.get_template('test.html')
    send_mail('testing mail', 'Testing is succesfully', 'arity.php@gmail.com', ['nemishpatel08@gmail.com'])
    return HttpResponse(template.render())