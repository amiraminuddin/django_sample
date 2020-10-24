from django.urls import path
from . import views

urlpatterns = [

    #route to views file and access the funtion
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
