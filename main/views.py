from .forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm


def login_view(request, newcontext={}):
    context = {"message": None}
    context.update(newcontext)
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {"message": 0})

    else:
        return render(request, 'login.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        return redirect('index')

    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        print("User is not authenticated and method = POST")
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        else:
            return render(request, 'signup.html', {"message": 0})
    else:
        print("Not authenticated and method = GET")
        return render(request, 'signup.html', {"message": None})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return login_view(request, newcontext={"message": 1})
    else:
        return redirect('login')


def setup_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            redirect('profile')


def profile(parameter_list):
    pass
