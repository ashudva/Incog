from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post, Comment, Reply

# Create your views here.
def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = post.comment_set.all()
    # replyset = []
    # if comment:
    #     for c in comment:
    #         replyset.append(c.reply_set.all())
    context = {
        "id": post_id,
        "comments": comment,
        # "replies": replyset,
        "posts": post
    }
    return render(request, 'index.html', context)
