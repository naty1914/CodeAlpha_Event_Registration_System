from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event, Registration

def events(request):
    events = Event.objects.all()
    return render(request, 'event/events.html', {'events': events})

def event_details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event/event_details.html', {'event': event})
def register(request):
    return render(request, 'event/register.html')