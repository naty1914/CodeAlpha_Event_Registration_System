from django.shortcuts import render
from django.http import HttpResponse

def events(request):
    return render(request, 'event/events.html')

def register(request):
    return render(request, 'event/register.html')