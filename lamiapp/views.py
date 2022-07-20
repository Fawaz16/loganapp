from django.shortcuts import render

from django.http import JsonResponse
import json
import datetime
from lamiapp.models import event_pic, main_page_pic, potraits,projects,booking,droneshot

# Create your views here.

def home(request):
    '''render home'''
    my_topic=main_page_pic.objects.all()

    return render(request, 'index.html',{'topic':my_topic})


def contact(request):
    '''render contact page'''
    return render(request, 'contact.html')


def potrait(request):
    '''render home'''
    new_topic=potraits.objects.all()

    return render(request, 'portfolio.html',{'topics':new_topic})
def event(request):
    '''render home'''
    event=event_pic.objects.all()

    return render(request, 'event.html',{'topic':event})

def projet(request):
    '''render project page'''
    project=projects.objects.all()
    return render(request, 'port.html',{'project':project})

def gallery(request,post_id):
    '''render gallery page'''
    print(post_id)
    project_1=projects.objects.get(id=post_id)
    return render(request,'gallery.html',{'project':project_1})

def bookings(request):
    '''render booking page'''
    book=booking.objects.all()
    return render(request, 'booking.html',{'booking':book})


def drone_shot(request):
    '''render drone  shots'''
    drone=droneshot.objects.all()
    return render(request, 'drone.html',{'drones':drone})






