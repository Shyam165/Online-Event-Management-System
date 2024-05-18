from django.shortcuts import render,redirect
from . models import Event
from .forms import BookingForm
from datetime import datetime
from .models import Contact
from django.contrib import messages
from .models import Feedback
from django.utils.dateparse import parse_date

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)
def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def feedback_view(request):
    if request.method == 'POST':
        event_name = request.POST.get('eventName')
        date = parse_date(request.POST.get('date'))
        platform = request.POST.get('platform')
        overall_experience = int(request.POST.get('overallExperience'))
        enjoyed_most = request.POST.get('enjoyedMost')

        feedback = Feedback(
            event_name=event_name,
            date=date,
            platform=platform,
            overall_experience=overall_experience,
            enjoyed_most=enjoyed_most
        )
        feedback.save()
        messages.success(request, 'Thank you for your feedback!')
        # return redirect('/') 

    return render(request, 'feedback.html')