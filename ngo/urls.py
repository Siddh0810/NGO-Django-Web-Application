from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("team/",views.team,name="team"),
    path("join/",views.join,name="join"),
    path("donate/",views.Donate,name="donate"),
    path("review/",views.Suggest,name="review"),
]
