"""lewa URL Configuration
    A hypothetical virtual school.
    Operation of this school is broken down into different modules
    Attendance - tracks the attendance record per student
    Calculator - uses provided input to compute a student's cummulative GPA
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('attendance.urls')),
    path('admin/', admin.site.urls),
]
