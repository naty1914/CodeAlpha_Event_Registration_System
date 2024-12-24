from django.shortcuts import render
from django.http import HttpResponse

def events(request):
    return HttpResponse('<h1>hello events here</h1.')

def register(request):
    return HttpResponse('<h1>hello register here</h1.')