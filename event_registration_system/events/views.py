from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Event, Registration
from .forms import RegistrationForm
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

def events(request):
    events = Event.objects.all()
    return render(request, 'event/events.html', {'events': events})
def event_details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event/event_details.html', {'event': event})

def register(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, fields=['username', 'email'])
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.token = get_random_string(32)
            try:
                registration.save()
                relative_url = reverse('manage_registration', args=[registration.token])
                confirmation_email = request.build_absolute_uri(relative_url)
                subject = 'Event Registration Confirmation'
                message = f"Please click the link below to confirm your registration for the event: {event.name} {confirmation_email}"
                from_email = 'nati@gmail.com'
                recipient_email = [registration.email]
                send_mail(subject, message, from_email, recipient_email, fail_silently=False)
                return render(request, 'event/registration_success.html', {'event': event })
            except ValidationError as e:
                 return HttpResponse(f'Registration failed: {e.message}')
    else:
        form = RegistrationForm(fields=['username', 'email'])
        context = {'form': form, 'event': event}
        return render(request, 'event/register.html', context)
    
def manage_registration(request, token):
    registration = get_object_or_404(Registration, token=token)
    if request.method == 'POST':
        subject = "Event Registration Cancelled"
        message = f"Your registration for the event: {registration.event.name} has been cancelled."
        from_email = 'nati@gmail.com'
        recipient_email = [registration.email]
        send_mail(subject, message, from_email, recipient_email, fail_silently=False)
        registration.delete()
        return render(request, 'event/registration_cancelled.html', {'registration': registration})
    else:
        return render(request, 'event/manage_registration.html', {'registration': registration})
    
            
            
            