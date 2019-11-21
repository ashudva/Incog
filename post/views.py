from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Reply
from main.models import Profile
from .forms import PostForm, CommentForm, ReplyForm
from django.utils import timezone
# Create your views here.


@login_required(login_url='accounts/login/')
def index_view(request):
    # Get list of all posts
    p = reversed(get_list_or_404(Post))
    # profile = Profile.objects.get(owner=request.user.id)
    context = {
        "posts": p,
        # "profile": profile,
        "post": PostForm(),
        "comment": CommentForm(),
        "reply": ReplyForm(),
    }
    return render(request, 'index.html', context)


@login_required(login_url='accounts/login/')
def new_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            heading = post.cleaned_data['heading']
            text = post.cleaned_data['text']
            p = Post(heading=heading, text=text,
                     author=request.user, pub_date=timezone.now())
            p.save()
        return redirect('index')

    return redirect('index')


@login_required(login_url='accounts/login/')
def new_comment(request):
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        # print(comment.text)
        if comment.is_valid():
            text = comment.cleaned_data['text']
            post_id = request.POST.get('post_id')
            parent_post = Post.objects.get(id=post_id)
            c = Comment(author=request.user, parent_post=parent_post, text=text,
                        pub_date=timezone.now())
            c.save()
        return redirect('index')

    return redirect('index')


@login_required(login_url='accounts/login/')
def new_reply(request):
    if request.method == 'POST':
        reply = ReplyForm(request.POST)
        # print(reply)
        if reply.is_valid():
            text = reply.cleaned_data['text']
            comment_id = request.POST.get('comment_id')
            parent_comment = Comment.objects.get(id=comment_id)
            c = Reply(author=request.user, text=text,
                      pub_date=timezone.now(), parent_comment=parent_comment)
            c.save()
        return redirect('index')

    return redirect('index')
