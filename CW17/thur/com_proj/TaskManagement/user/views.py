from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', context={'form': form})
