from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Event, Registration
from .forms import RegistrationForm
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

def events(request):
    events = Event.objects.all()
    return render(request, 'event/events.html', {'events': events})
def event_details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event/event_details.html', {'event': event})

def register(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.token = get_random_string(32)
            registration.save()
            relative_url = reverse('manage_registration', args=[registration.token])
            confirmation_email = request.build_absolute_uri(relative_url)
            subject = 'Event Registration Confirmation'
            message = f"Please click the link below to confirm your registration for the event: {event.name} {confirmation_email}"
            from_email = 'nati@gmail.com'
            recipient_email = [registration.email]
            send_mail(subject, message, from_email, recipient_email, fail_silently=False)
            return HttpResponse('registration successful')
    else:
        form = RegistrationForm()
        context = {'form': form, 'event': event}
        return render(request, 'event/register.html', context)
    
@csrf_exempt
def manage_registration(request, token):
    
    registration = get_object_or_404(Registration, token=token)
    if request.method == 'POST':
        registration.delete()
        return HttpResponse('Registration hab been  cancelled')
    else:
        return HttpResponse(f'Managing registration for: {registration.username}. To cancel, submit a POST request.')
    
            
            
            