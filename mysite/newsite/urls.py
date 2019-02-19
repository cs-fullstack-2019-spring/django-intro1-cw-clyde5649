from django.urls import path,include

from . import views

# this is wear i put my code for the user to click on it to show up i linked it
urlpatterns = [
    path('', views.index, name='index'),
    path("music/", include("newsite.py"),