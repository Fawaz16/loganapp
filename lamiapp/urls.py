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
    path('gallery/<int:post_id>',views.gallery,name='gallery'),
   
]
