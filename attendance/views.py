from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.
def attendance(request):
    return HttpResponse("Wow this is an <strong>awesome</strong> app")

def register(request):
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
