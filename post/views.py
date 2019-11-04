from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from .models import Post, Comment, Reply
# Create your views here.
def post_view(request):
    if request.user.is_authenticated:
        # Get list of all posts
        p = get_list_or_404(Post)
        context = {
            "posts": p
        }
        return render(request, 'index.html', context)
    return render(request, 'login.html', {"message": None})
