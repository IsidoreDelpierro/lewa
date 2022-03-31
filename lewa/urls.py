"""lewa URL Configuration
    A hypothetical virtual school.
    Operation of this school is broken down into different modules
    Attendance - tracks the attendance record per student
    Calculator - uses provided input to compute a student's cummulative GPA
"""
from django.contrib import admin
from django.urls import path, include
from administration import views as administrator
from academics import views as academic

urlpatterns = [
    path('attend/', include('attendance.urls')),

    path('', academic.studentDashboard, name="student_dashboard"),
    path('staff/', academic.staffDashboard, name="staff_dashboard"),
    path('teacher/', academic.teacherDashboard, name="teacher_dashboard"),
    path('admin/', administrator.dashboard, name="admin_dashboard"),
    path('dev/', admin.site.urls),
]
