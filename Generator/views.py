from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def Poorya(request):
    return HttpResponse('<h1>My name is poorya mohammadi nasab</h1>')