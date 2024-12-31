from django.forms import ModelForm
from .models import Registration
from django.core.exceptions import ValidationError
class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__' 
    
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        if fields:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                print(field_name)
                self.fields.pop(field_name)
    def clean(self):
        cleaned_data = super().clean()
        event = cleaned_data.get('event')
        email = cleaned_data.get('email')

        if Registration.objects.filter(event=event, email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Registration for this event already exists")

        return cleaned_data