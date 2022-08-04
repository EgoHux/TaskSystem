from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from authapp.forms import CustomUserLoginForm, CustomUserCreationForm, CustomUserChangeForm, UserDataForm
from authapp.models import CustomUser, UserData
from django.utils.timezone import now
# Create your views here.


def login(request):
    form = CustomUserLoginForm()

    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
                LastAuthDate = now()
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

def account(request):

    try:
        userdata = UserData.objects.get(user=request.user)
    except:
        userdata = UserData.objects.create(user=request.user, gender="M")

    userform = CustomUserChangeForm(instance = request.user)
    userdataform = UserDataForm(instance = userdata)

    if request.method =="POST":
        userform = CustomUserChangeForm(instance=request.user, data=request.POST)
        userdataform = UserDataForm(instance=userdata, data=request.POST)

        if userform.is_valid() and userdataform.is_valid():
            userform.save()
            userdataform.save()
            return HttpResponseRedirect(reverse('main'))

    return render(request, 'authapp/account.html', context={
        'title': "Мой аккаунт",
        'userform': userform,
        'userdataform':userdataform
    })


def create_user(request):
    userform = CustomUserCreationForm()
    if request.method == 'POST':
        userform = CustomUserCreationForm(data=request.POST)

        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(reverse('all_users'))

    return render(request, 'authapp/create_user.html', context={
        'title': 'Создание аккаунта',
        'userform': userform
    })