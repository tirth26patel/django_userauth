from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .forms import AppointmentForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def setcookie(request):
    response = render(request, 'setcookie.html')
    # max_age=60
    response.set_cookie('lname','patel', expires= datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name', "nahi hai bhai")
    return render(request, 'getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response



def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Assuming user is logged in
            appointment.save()
            return redirect('appointment_confirmation')  # Redirect to a confirmation page
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})

from .forms import AppointmentForm
from .models import Appointment
from django.db.models import Q

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Assuming user is logged in

            # Check for overlapping appointments
            overlapping_appointments = Appointment.objects.filter(
                Q(date=appointment.date) &
                ((Q(start_time__lt=appointment.end_time) & Q(end_time__gt=appointment.start_time)) |
                 (Q(start_time__lte=appointment.start_time) & Q(end_time__gte=appointment.end_time)))
            )

            if overlapping_appointments.exists():
                # Handle overlapping appointments error
                return render(request, 'overlap_error.html')

            appointment.save()
            return redirect('appointment_confirmation')  # Redirect to a confirmation page
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})



