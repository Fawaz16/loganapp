from django.shortcuts import render, redirect

from django.http import JsonResponse
import json
import datetime
from lamiapp.models import event_pic, main_page_pic, potrait_pic,project,booking,droneshot
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            name = form.cleaned_data['Name']
            package = form.cleaned_data['Package']
            message = form.cleaned_data['Message']
            number = form.cleaned_data['Number']

            # Render the email template with the form data
            email_html = render_to_string('email.html', {
                'name': name,
                'email': email,
                'package': package,
                'message': message,
                'number': number,
            })

            # Send email to the sender
            send_mail(
                f'Hello {name}',
                'We have now received your details and will get in touch as soon as possible',
                'fawazrufai5@gmail.com',  # Replace with your email address
                [email],  # Sender's email address
                html_message=email_html,
            )

            # Send email to the recipient
            send_mail(
                f'New Booking: {name}',
                'A new booking has been made.',
                'fawazrufai5@gmail.com',  # Replace with your email address
                [email],  # Recipient's email address
                html_message=email_html,
            )

            print('Your message has been sent')
            return redirect('bookings')
    else:
        form = ContactForm()
        
    return render(request, 'bookings.html', {'form': form})
def drone_shot(request):
    '''render drone  shots'''
    drone=droneshot.objects.all()
    return render(request, 'drone.html',{'drones':drone})






