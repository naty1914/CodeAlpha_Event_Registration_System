""" Test module for events app """
from django.test import TestCase
from .models import Event, Registration
from .forms import RegistrationForm

class EventModelTest(TestCase):
    """ Test class for Event model """
    def setUp(self):
        """ Create an event object """
        self.event = Event.objects.create(name="Test Event", description='This is a test event description', location='22')
        
    def test_event_creation(self):
        """ Test Event model creation """
        self.assertEqual(self.event.name, 'Test Event')
        self.assertEqual(self.event.description, 'This is a test event description')
        self.assertEqual(self.event.location, '22')
        
class RegistrationModelTest(TestCase):
    """ Test class for Registration model """
    def setUp(self):
        """ Create an event and registration object """
        self.event = Event.objects.create(name="event2", description='This is a test event2 description', location='test')
        self.registration = Registration.objects.create(event = self.event, email='test@gmail.com', username='test123')
    
    def test_registration_creation(self):
        """ Test Registration model creation """
        self.assertEqual(self.registration.event.name, 'event2')
        self.assertEqual(self.registration.email, 'test@gmail.com')
        self.assertEqual(self.registration.username, 'test123')
    
class RegistrationFormTest(TestCase):
    """ Test class for Registration form """
    def setUp(self):
        """ Create an event object """
        self.event = Event.objects.create(name='event3', description='This is a test event 3 description', location='test3')
    
    def test_registration_form(self):
        """ Test Registration form """
        form_data = {
            'event': self.event,
            'email': 'test@gmail.com',
            'username': 'test123',
            'date': '2024-12-12',
            'token': 'testtoken',   
        }
        form = RegistrationForm(form_data)
        self.assertTrue(form.is_valid())