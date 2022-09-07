import imp
from django import views
from django.urls import path,include
from  .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('potrait/',views.potrait,name='potrait'),
    path('event/',views.event,name='event'),
    path('projet/',views.projet,name='projet'),
    path('general/',views.general,name='general'),
    path('bookings/',views.bookings,name='bookings'),
    
    path('drone_shot/',views.drone_shot,name='drone_shot'),
    path('gallery/<int:post_id>',views.gallery,name='gallery'),
   
]
