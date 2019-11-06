from django import forms
from post.models import Post, Comment, Reply
from .models import Profile
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password again'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password


class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class ReportForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_visibility', 'birth_date', 'bio',
                  'status', 'philosophy', 'dream', 'ambition']
