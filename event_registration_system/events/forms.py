from django.forms import ModelForm
from .models import Registration

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = {'username', 'email'} 