from .models import Profile
from django import forms


class PostForm(forms.Form):

    class Meta:
        model = Post
        fields = ['confession', 'heading']


class commentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['text']
