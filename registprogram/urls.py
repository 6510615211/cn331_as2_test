from django.urls import path
from registprogram import views
urlpatterns = [
    path('', views.index),
    path('course' , views.course)
]