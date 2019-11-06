from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Reply
# Create your views here.

@login_required(login_url = '/login/')
def post_view(request):
    # Get list of all posts
    p = get_list_or_404(Post)
    context = {
        "posts": p
    }
    return render(request, 'index.html', context)
