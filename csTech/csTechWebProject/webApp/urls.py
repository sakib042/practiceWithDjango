from django.urls import path
from . import views

app_name = "webApp"

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('tutorial', views.tutorial, name='tutorial')
]