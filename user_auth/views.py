from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SignUpForm

def user_login(request):
    """
    View for user login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to user details page upon successful login
            return redirect('user_auth:user_details')
        else:
            return render(request, 'authentication/login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'authentication/login.html')

def register_user(request):
    """
    View for user registration.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to user details page after successful registration
            return redirect('user_auth:user_details')
    else:
        form = SignUpForm()
    return render(request, 'authentication/register.html', {'form': form})

def authenticate_user(request):
    """
    View for authenticating user.
    """
    return render(request, 'authentication/user.html')

def show_user(request):
    """
    View to display user details.
    """
    if request.user.is_authenticated:
        return render(request, 'authentication/user.html', {'username': request.user.username})
    else:
        return redirect('user_auth:login')
