from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('About Page')

def contact(request):
    return HttpResponse('Contact Page')