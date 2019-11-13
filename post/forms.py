from .models import Comment, Post, Reply
from django import forms
from django.utils import timezone


class PostForm(forms.Form):
    heading = forms.CharField(max_length=100)
    confession = forms.CharField(max_length=2000)

    # def clean(self, request):
    #     heading = self.cleaned_data['heading']
    #     confession = self.cleaned_data['confession']
    #     author = request.user.username
    #     pub_date = timezone.now()

    #     else:
    #         return (heading, confession, author, pub_date)


class CommentForm(forms.Form):
    text = forms.CharField(max_length=200)


class ReplyForm(forms.Form):
    text = forms.CharField(max_length=200)
