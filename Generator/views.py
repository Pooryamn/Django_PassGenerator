from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'9621160025'})

def password(request):
    return render(request,'generator/password.html')