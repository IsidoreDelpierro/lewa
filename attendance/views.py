from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .models import Attend
from django.utils import timezone

def attendance(request):
    return HttpResponse("Wow this is an <strong>awesome</strong> app")

def register_view(request):
    if request.method == "POST":
        print("POST Request received")
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is Valid")
            form.save()
    else:
        print("GET Request received")
        form = UserRegistrationForm()

    return render(request, "attendance/register.html", {'form': form})


def attend_view(request):
    status = None
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                #Pick out all attend objects for current user
                attended_datetime = str(timezone.now())[:10]
                print(attended_datetime)
            except:
                pass

            #Filter out current user who attended today
            attended_today = Attend.objects.filter(attender=request.user, datetime__startswith=attended_datetime)

            if str(attended_today)[10:] == "[]>":
                status = 3

            else:
                status = 2

            if status == 3:
                attend_object = Attend(attender=request.user)
                attend_object.save()
                status = 1

    else:
        #User hasn't logged in
        status = 0

    return render(request, "attendance/attend.html", {'status' : status})
