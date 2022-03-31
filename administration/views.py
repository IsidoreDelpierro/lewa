from django.shortcuts import render

# Create your views here.

def dashboard(request):
    pagetitle = "Admin Dashboard"
    context = {'pagetitle':pagetitle}
    return render(request, 'administration/dashboardadmin.html', context)
