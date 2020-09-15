from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.


def home(request):
    return HttpResponse('<h1> This is the Home page </h1>')


def about(request):
    return HttpResponse('<h1> This is the About me page </h1>')


def github(request):
    return HttpResponse('<h1> This is the Github Page </h1>')
