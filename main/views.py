from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from post.views import post_view
# Create your views here.

def login_view(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(post_view)
    else:
        return render(request, 'login.html', {"message": 1})

def signup_view(request):
    if not request.user.is_authenticated:
        return render(request, 'signup.html', {})
    else:
        return redirect(post_view)

def logout_view(request):
    logout(request)
    return render(request, 'login.html', {"message": 0})

def index(request):
    if  not request.user.is_authenticated:
        return render(request, 'login.html', {"message": None})
    return redirect(post_view)
