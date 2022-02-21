"""lewa URL Configuration
    Attendance module for our virtual school
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import attend_view

app_name = "attendance"

urlpatterns = [
    path("", views.attendance, name="attendance"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="attendance/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="attendance/logout.html"), name="logout"),
    path("attend/", attend_view, name="attend_view")
]
