from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.forms import LoginUserForm


def login_user(request):
    success_url = reverse_lazy('home')
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect(success_url)
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    success_url = reverse_lazy('users:login')
    return redirect(success_url)
