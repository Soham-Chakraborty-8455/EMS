from django.contrib import admin
from django.urls import path
from EMSapp import views

urlpatterns = [
    path("", views.index, name="ServerSide"),
]