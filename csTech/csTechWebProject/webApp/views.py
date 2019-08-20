from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


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
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f"New Account Created: {username}")
            messages.success(request, f"{username} has been logged In!")
            login(request, user)
            return redirect("webApp:tutorial")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    requested_page_location = 'webApp/registration.html'
    form = NewUserForm()
    return render(request, requested_page_location, context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"{username} has been logged In!")
                return redirect("webApp:tutorial")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")

    requested_page_location = 'webApp/login.html'
    form = AuthenticationForm()
    return render(request, requested_page_location, context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out Successfully!")
    return redirect("webApp:home")