from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music', views.music, name='artist'),
    path('Wale', views.Wale, name='artist'),
    path('usher', views.Usher, name='artist'),
    path('Meek ', views.Meek, name='artist')
]