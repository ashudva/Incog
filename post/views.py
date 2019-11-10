from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Reply
from main.models import Profile
# Create your views here.


@login_required(login_url='accounts/login/')
def index_view(request):
    # Get list of all posts
    p = get_list_or_404(Post)
    profile = Profile.objects.get(owner=request.user.id)
    context = {
        "posts": p,
        "profile": profile
    }
    return render(request, 'index.html', context)


@login_required(login_url='accounts/login/')
def frontend(request):
    profile = Profile.objects.get(id=1)
    return render(request, 'home.html', {"profile": profile})
