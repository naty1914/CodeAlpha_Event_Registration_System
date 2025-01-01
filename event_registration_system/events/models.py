from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.exceptions  import ValidationError
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    token = models.CharField(max_length=32, unique=True, default=get_random_string(32))
    
    def __str__(self):
        return f"{self.username} - {self.event.name} - {self.date.date()}"

    def save(self, *args, **kwargs):
        
        if self.event.id is None:
            raise ValidationError("Event ID is required")
        
        if self.email is None:
            raise ValidationError("Event email is required")
        
        if Registration.objects.filter(event=self.event, email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError("Registration for this event already exists")
        
        if  len(self.username) > 100:
            raise ValidationError("Username must be less than 100 characters")
        
        if not self.token or not self.pk:
            self.token = get_random_string(32)
        super().save(*args, **kwargs)
