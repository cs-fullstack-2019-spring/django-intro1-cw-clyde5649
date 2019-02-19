from django.urls import path,include

from . import views
# let my user know where they need to go
urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music, name='index'),
    path('Wale/', views.Wale, name='index'),
    path('usher/', views.Usher, name='index'),
    path('Meek/', views.Meek, name='index')
]