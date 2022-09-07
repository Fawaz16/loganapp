from django.shortcuts import render

from django.http import JsonResponse
import json
import datetime
from lamiapp.models import event_pic, main_page_pic, potrait_pic,project,booking,droneshot

# Create your views here.

def home(request):
    '''render home'''

    return render(request, 'index.html')

def general(request):
    ''''render general image'''
    main=main_page_pic.objects.all()
    return render(request, 'gallery2.html', {'main':main})


def contact(request):
    '''render contact page'''
    return render(request, 'contact.html')


def potrait(request):
    '''render home'''
    new_topic=potrait_pic.objects.all()

    return render(request, 'portfolio.html',{'topics':new_topic})
def event(request):
    '''render home'''
    event=event_pic.objects.all()

    return render(request, 'event.html',{'topic':event})

def projet(request):
    '''render project page'''
    projects=project.objects.all()
    return render(request, 'booking.html',{'project':projects})

def gallery(request,post_id):
    '''render gallery page'''
    print(post_id)
    project_1=project.objects.get(id=post_id)
    return render(request,'gallery.html',{'project':project_1})

def bookings(request):
    '''render booking page'''
    return render(request, 'port.html')


def drone_shot(request):
    '''render drone  shots'''
    drone=droneshot.objects.all()
    return render(request, 'drone.html',{'drones':drone})






