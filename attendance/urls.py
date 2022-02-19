"""lewa URL Configuration
    Attendance module for our virtual school 
"""
from django.urls import path
from . import views

app_name = "attendance"

urlpatterns = [
    path("", views.attendance, name="attendance"),

]
