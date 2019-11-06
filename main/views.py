from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.template import Context


def login_view(request, newcontext = {}):
    context = Context({"message": None})
    context.update(newcontext)
    if request.user.is_authenticated:
        return redirect('post')
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post')
        else:
            return render(request, 'login.html', {"message": 1})

    else:
        return render(request, 'login.html', {"message": 1})

def signup_view(request):
    if (not request.user.is_authenticated) and (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if form.is_valid():
            raw_username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            if User.objects.get(username=raw_username) is not None:
                return render(request, 'singup.html', {"message": 0, "username": raw_username})
            else:
                form.save()
                user = authenticate(username=username, password=raw_password)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('post')
    else:
        return render(request, 'signup.html', {"message": None})

    # if not request.user.is_authenticated:
    #     return render(request, 'signup.html', {})
    # else:
    #     return redirect('index')


def logout_view(request,):
    if request.user.is_authenticated:
        logout(request)
        return redirect(login_view(request, newcontext = {"message": 0}))
    else:
        return render(request, 'login.html', {"message": None})


def index(request):
    if  not request.user.is_authenticated:
        return redirect(login_view(request, newcontext = {"message": 2}))
    return redirect('post')
