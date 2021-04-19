from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request): #HOME
    return render(request,"Eldatononoapp/home.html")

def registro(request): #REGISTRO
    
    return render(request,"Eldatononoapp/registro.html")

def login(request): #LOGIN
    
    return render(request,"Eldatononoapp/login.html")