from django.urls import path
from . import views

app_name = "webApp"

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('tutorial', views.tutorial, name='tutorial'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path("<single_slug>", views.single_slug, name="Single_Slug"),
]