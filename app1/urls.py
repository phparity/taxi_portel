from django.contrib import admin
from django.urls import path, include

from app1 import views




urlpatterns = [
    path('',views.home , name='home'),
    path('map/', views.draw_area_on_map, name='map'),
    path('check_zone/', views.check_zone, name='check_zone'),
    path('showzone/<int:id>/', views.showzone, name='showzone'),
   
]