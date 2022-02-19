from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def attendance(request):
    return HttpResponse("Wow this is an <stron>awesome</strong> app")
