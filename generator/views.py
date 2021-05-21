from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('Special'):
        characters.extend('#@!%&^+_}')
    
    if request.GET.get('Numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')