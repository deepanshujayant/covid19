from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.
from .models import Corona
from .forms import OrderForm, CreateUserForm


@csrf_exempt
def home(request):
    #print("Running")
    if request.method == 'POST':
       username = request.POST.get('username')
       print(username)
       password = request.POST.get('password')
       print(password)
       user = authenticate(username = username, password = password)
       print(user)
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
    print("Hello")
    if request.user.is_authenticated:
        return redirect('/main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                print(form)
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
    #sdata = True
    result = None
    countryPick  = None
    countrydata = request.GET.get("country") or 'India'
    print(countrydata)

    result = requests.get('https://api.covid19api.com/summary')
    json = result.json()

    countryPick = json['Countries']
    #print(countryPick)
    for i in countryPick:
        #print(print(i['Country']))
        if(i['Country'] == countrydata):
            print(i)
            return render(request, 'Country.html', {'countryPick' : i, 'data': countryPick})

            
        
        
    

