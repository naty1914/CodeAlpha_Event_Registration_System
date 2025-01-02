"""URLs for the events app"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('register/<int:id>', views.register, name='register'),
    path('event/<int:id>', views.event_details, name='event_details'),
    path('manage_registration/<str:token>', views.manage_registration, name='manage_registration'),
    path('contact/', views.contact, name='contact')
]