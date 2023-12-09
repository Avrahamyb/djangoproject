from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'pages/index.html')



def all_reminders(request):
    reminders = Reminder.objects.all()
    return render(request, 'pages/all_reminders.html', {'reminders' : reminders})


