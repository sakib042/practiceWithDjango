from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def home(request):
    requested_page_location = 'webApp/home.html'
    return render(request, requested_page_location)


def about(request):
    requested_page_location = 'webApp/about.html'
    return render(request, requested_page_location)


def tutorial(request):
    requested_page_location = 'webApp/tutorial.html'
    return render(request=request, template_name=requested_page_location, context={"tutorials": Tutorial.objects.all})


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect("webApp:tutorial")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    requested_page_location = 'webApp/registration.html'
    form = UserCreationForm
    return render(request, requested_page_location, context={"form":form})