from django import forms

class PostForm(forms.ModelForm):

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
