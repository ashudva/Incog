from .models import Comment, Post, Reply
from django import forms


class PostForm(forms.Form):
    heading = forms.CharField(max_length=100)
    confession = forms.CharField(max_length=2000)

    def clean(self):
        pass

    def get_auto_data(self):
        pass


class CommentForm(forms.Form):
    text = forms.CharField(max_length=200)


class ReplyForm(forms.Form):
    text = forms.CharField(max_length=200)
