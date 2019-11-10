from django.shortcuts import render
from .forms import ProfileForm
# Create your views here.


def forms_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            bio = form.cleaned_data['bio']
            email = form.cleaned_data['email']
            cc = form.cleaned_data['cc']
            context = {
                "ln": last_name,
                "fn": first_name,
                "bio": bio,
                "email": email,
                "cc": cc
            }
            return render(request, 'form_view.html', context)

        else:
            return render(request, 'form.html', {"form": form})
    else:
        form = ProfileForm()

    return render(request, 'form.html', {"form": form})
