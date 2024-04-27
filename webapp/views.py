from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def signup_page(request):
    return render(request, 'registration/signup.html')  # Render the signup template from accounts app

def login_page(request):
    return render(request, 'authentication/login.html')  # Render the login template from user_auth app
