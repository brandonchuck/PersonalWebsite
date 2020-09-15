from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.


def home(request):
    # render takes "request", and html template found in app subdir of templates folder
    # render can also take a dictionary as its last arg
    return render(request, 'portal/home.html')


def about(request):
    return render(request, 'portal/aboutme.html')


def github(request):
    return HttpResponse('<h1> This is the Github Page </h1>')
