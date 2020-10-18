from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.
from .models import Corona
from .forms import OrderForm, CreateUserForm



def home(request):
    #print("Running")
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username = username, password = password)
       if user is not None:
            login(request, user)
            return redirect('/main')
       else:
           messages.info(request,'Username or Password Incorrect!!')
           #return redirect('/')

    return render(request, 'Home.html')

        

def logoutUser(request):
    logout(request)
    return redirect('/')
    #return redirect('/main')
    #return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/')  

        return render(request, 'register.html', {'form':form})

@login_required(login_url='/logout') #copy paste this line for next def of country data
def covid(request):
    data1 = True
    result1 = None
    covidCases = None
    while(data1):
        try:
            result1 = requests.get('https://api.covid19api.com/summary')
            json = result1.json()
            
            covidCases = json['Global']
            data1 = False
        except:
            data1 = True

    return render(request, 'Main.html', 
    {'covidCases' : covidCases})


@login_required(login_url='/logout')
def countryData(request):
    data = True
    result = None
    countryPick  = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
            countryPick = json['Countries']
            data = False
        except:
            data = True
    return render(request, 'Country.html', {'countryPick' : countryPick})