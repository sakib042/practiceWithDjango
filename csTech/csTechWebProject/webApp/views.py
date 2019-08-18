from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
# Create your views here.

def home(request):
    requested_page_location = 'webApp/home.html'
    return render(request, requested_page_location)

def about(request):
    requested_page_location = 'webApp/about.html'
    return render(request, requested_page_location)

def tutorial(request):
    requested_page_location = 'webApp/tutorial.html'
    return render(request=request, template_name=requested_page_location, context={"tutorials": Tutorial.objects.all})
