from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'9621160025'})

def password(request):

    GenPass = ''

    LowerChars = string.ascii_lowercase
    
    lenght = 10

    for i in range(lenght):
        GenPass += random.choice(LowerChars)

    return render(request,'generator/password.html',{'password':GenPass})