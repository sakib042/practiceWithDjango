from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


def single_slug(request, single_slug):
    requested_page_location = 'webApp/category.html'
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(category_name__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series_name__tutorial_series_name=m.tutorial_series_name).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        return render(request, requested_page_location, {"part_ones": series_urls})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorial_from_series = Tutorial.objects.filter(tutorial_series_name__tutorial_series_name=this_tutorial.tutorial_series_name).order_by("tutorial_published")
        this_tutorial_idx = list(tutorial_from_series).index(this_tutorial)
        return render(request, "webApp/tutorial.html", {"tutorial": this_tutorial, "sidebar": tutorial_from_series, "this_tutorial_idx": this_tutorial_idx})

    return HttpResponse("does not have any")


def home(request):
    requested_page_location = 'webApp/categories.html'
    return render(request, requested_page_location, context={'categories': TutorialCategory.objects.all})


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
                return redirect("webApp:home")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")

    requested_page_location = 'webApp/login.html'
    form = AuthenticationForm()
    return render(request, requested_page_location, context={"form": form})


def logout_request(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect("webApp:login")
