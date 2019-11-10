from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=64, label="First Name")
    last_name = forms.CharField(max_length=64, label="Last Name")
    email = forms.EmailField(required=False)
    bio = forms.CharField(widget=forms.Textarea, max_length=10)
    cc = forms.BooleanField(required=False)
