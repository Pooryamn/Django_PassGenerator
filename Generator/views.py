from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'9621160025'})

def password(request):

    GenPass = ''

    valid_Chars = string.ascii_lowercase #at first the only valid characters are lowercases

    if (request.GET.get('UpperCase')):
        valid_Chars += string.ascii_uppercase
    
    if (request.GET.get('Special')):
        valid_Chars += '!@#$%&*():/?.-+<>'

    if (request.GET.get('Numbers')):
        valid_Chars += '0123456789'

    
    lenght = int(request.GET.get('length',12)) # get lenght from web

    for i in range(lenght):
        GenPass += random.choice(valid_Chars)

    return render(request,'generator/password.html',{'password':GenPass})

def info(request):
    return render(request,'generator/info.html')