from django.contrib import admin
from .models import Event, Registration
from .forms import RegistrationForm

class RegistrationAdmin(admin.ModelAdmin):
    form = RegistrationForm
    list_display = ('username', 'event', 'email', 'date')

admin.site.register(Event)
admin.site.register(Registration, RegistrationAdmin)