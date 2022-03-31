from django.shortcuts import render

# Create your views here.

def studentDashboard(request):
    pagetitle = "Student Dashboard"
    context = {'pagetitle':pagetitle}
    return render(request, 'academics/dashboardstudent.html', context)

def staffDashboard(request):
    pagetitle = "Staff Dashboard"
    context = {'pagetitle':pagetitle}
    return render(request, 'academics/dashboardstaff.html', context)

def teacherDashboard(request):
    pagetitle = "Teacher Dashboard"
    context = {'pagetitle':pagetitle}
    return render(request, 'academics/dashboardteacher.html', context)
