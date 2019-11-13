from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Reply
from main.models import Profile
from .forms import PostForm, CommentForm, ReplyForm
# Create your views here.


@login_required(login_url='accounts/login/')
def index_view(request):
    # Get list of all posts
    p = get_list_or_404(Post)
    profile = Profile.objects.get(owner=request.user.id)
    context = {
        "posts": p,
        "profile": profile,
        "post": PostForm(),
        "comment": CommentForm(),
        "reply": ReplyForm(),
    }
    return render(request, 'index.html', context)


@login_required(login_url='accounts/login/')
def new_post(request):
    if request.method == 'POST':
        heading = request.POST.get('heading', False)
        confession = request.POST.get('confession', False)
        print(heading)
        print(confession)
        return redirect('index')

    return redirect('index')


@login_required(login_url='accounts/login/')
def new_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('text', False)
        print(comment)
        return redirect('index')

    return redirect('index')


@login_required(login_url='accounts/login/')
def new_reply(request):
    if request.method == 'POST':
        reply = request.POST.get('text', False)
        print(reply)
        return redirect('index')

    return redirect('index')
