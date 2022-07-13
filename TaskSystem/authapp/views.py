from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from authapp.forms import CustomUserLoginForm, CustomUserCreationForm

# Create your views here.


def login(request):
    form = CustomUserLoginForm()

    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )
            if user:
                auth.login(request, user=user)
                return HttpResponseRedirect(reverse('main'))

    return render(request, 'authapp/login.html', context={
        'title': "Вход в систему",
        'form': CustomUserLoginForm()
    })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


def register(request):
    form = CustomUserCreationForm()
    if request.method =='POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'authapp/register.html', context={
        'title': 'Регистрация аккаунта',
        'form': form
    })

