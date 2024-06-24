from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Event, Facility, Student, Admin, Registration, Booking
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.
def index(request):
    return render (request,"index.html")

def loginuser(request):
    error_message = None
    student = None

    if request.method == "POST":
        Studentname = request.POST.get('Studentname')
        Studentpass = request.POST.get('Studentpass')
        try:
            student = Student.objects.get(Studentname=Studentname, Studentpass=Studentpass)
        except Student.DoesNotExist:
            error_message = 'Invalid ID or password'

        if student:
            
            Studentname = student.Studentname
            homepageuser_url = reverse('homepageuser', args=[Studentname])
            return HttpResponseRedirect(homepageuser_url)

    return render(request, "loginuser.html",{'error_message': error_message})



def homepageuser(request, Studentname):
    students = Student.objects.all()
    try:
        student = Student.objects.get(Studentname = Studentname)
    except Student.DoesNotExist:
        return render(request, "loginuser.html",)
    
    return render(request, "homepageuser.html", {'student': student, 'students': students})

def event1(request):
    return render (request,"event1.html")

def event2(request):
    if request.method == 'POST':
        Studentname = request.POST.get('Studentname')
        Eventname = request.POST.get('Eventname')

        try:
            student = Student.objects.get(Studentname=Studentname)
            event = Event.objects.get(Eventname=Eventname)

            registration = Registration(
                student=student,
                event=event,
            )
            registration.save()

            messages.success(request, 'Registration successful!')
            return redirect('homepageuser', Studentname=Studentname)
        except Student.DoesNotExist:
            messages.error(request, 'Student does not exist.')
        except Event.DoesNotExist:
            messages.error(request, 'Event does not exist.')

    events = Event.objects.all()
    return render(request, 'event2.html', {'events': events})



def booking1(request):
    return render (request,"booking1.html")


def booking2(request):
    if request.method == 'POST':
        Studentname = request.POST.get('Studentname')
        Facilityname = request.POST.get('Facilityname')


        try:
            student = Student.objects.get(Studentname=Studentname)
            facility = Facility.objects.get(Facilityname=Facilityname)

            booking = Booking(
                student=student,
                facility=facility,
            )
            booking.save()

            messages.success(request, 'Booking successful!')
            return redirect('homepageuser', Studentname=Studentname)
        except Student.DoesNotExist:
            messages.error(request, 'Student does not exist.')
        except Facility.DoesNotExist:
            messages.error(request, 'Facility does not exist.')

    facilities = Facility.objects.all()
    return render(request, 'booking2.html', {'facilities': facilities})


def booking3(request):
    if request.method == 'POST':
        Studentname = request.POST.get('Studentname')
        Facilityname = request.POST.get('Facilityname')


        try:
            student = Student.objects.get(Studentname=Studentname)
            facility = Facility.objects.get(Facilityname=Facilityname)

            booking = Booking(
                student=student,
                facility=facility,
            )
            booking.save()

            messages.success(request, 'Booking successful!')
            return redirect('homepageuser', Studentname=Studentname)
        except Student.DoesNotExist:
            messages.error(request, 'Student does not exist.')
        except Facility.DoesNotExist:
            messages.error(request, 'Facility does not exist.')

    facilities = Facility.objects.all()
    return render(request, 'booking3.html', {'facilities': facilities})


def booking4(request):
    if request.method == 'POST':
        Studentname = request.POST.get('Studentname')
        Facilityname = request.POST.get('Facilityname')


        try:
            student = Student.objects.get(Studentname=Studentname)
            facility = Facility.objects.get(Facilityname=Facilityname)

            booking = Booking(
                student=student,
                facility=facility,
            )
            booking.save()

            messages.success(request, 'Booking successful!')
            return redirect('homepageuser', Studentname=Studentname)
        except Student.DoesNotExist:
            messages.error(request, 'Student does not exist.')
        except Facility.DoesNotExist:
            messages.error(request, 'Facility does not exist.')

    facilities = Facility.objects.all()
    return render(request, 'booking4.html', {'facilities': facilities})


def viewbooking(request):
    alldata = Booking.objects.all()
    dict={
        'alldata':alldata
    }
    return render (request,'viewbooking.html',dict)

def delete_bookingpage(request, bookingid):
    data = Booking.objects.get(bookingid=bookingid)
    data.delete()
    return HttpResponseRedirect(reverse("viewbooking"))


def loginadmin(request):
    error_message = None
    admin = None

    if request.method == "POST":
        Adminid = request.POST.get('Adminid')
        Adminpass = request.POST.get('Adminpass')
        try:
            admin = Admin.objects.get(Adminid=Adminid, Adminpass=Adminpass)
        except Admin.DoesNotExist:
            error_message = 'Invalid ID or password'

        if admin:
            
            Adminid = admin.Adminid
            adminhomepage_url = reverse('adminhomepage', args=[Adminid])
            return HttpResponseRedirect(adminhomepage_url)

    return render(request, "loginadmin.html",{'error_message': error_message})

def adminhomepage(request, Adminid):
    admins = Admin.objects.all()
    try:
        admin = Admin.objects.get(Adminid = Adminid)
    except Admin.DoesNotExist:
        return render(request, "loginadmin.html",)
    
    return render(request, "adminhomepage.html", {'admin': admin, 'admins': admins})