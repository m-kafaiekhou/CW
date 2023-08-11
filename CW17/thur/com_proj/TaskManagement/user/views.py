from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from django.views import View
from .models import CustomUser
# Create your views here.
from .mixins import OwnerRequiredMixin


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


class ProfileView(OwnerRequiredMixin, View):
    form_class = CustomUserChangeForm
    template_name = 'registration/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(instance=user)
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('profile', user.id)
