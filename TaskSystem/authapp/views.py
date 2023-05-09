from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from authapp.forms import CustomUserLoginForm, CustomUserCreationForm, CustomUserChangeForm, UserDataForm
from authapp.models import CustomUser, UserData, Right
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


# def login(request):
#     form = CustomUserLoginForm()

#     if request.method == 'POST':
#         form = CustomUserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = auth.authenticate(
#                 username = form.cleaned_data["username"],
#                 password = form.cleaned_data["password"],
#                 LastAuthDate = now()
#             )
        
#             if user:
#                 auth.login(request, user=user)
#                 return HttpResponseRedirect(reverse('main'))

#     return render(request, 'authapp/login.html', context={
#         'title': "Вход в систему",
#         'form': CustomUserLoginForm()
#     })

def login(request):
    form = CustomUserLoginForm()
    form_create = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        form_create = CustomUserCreationForm(data=request.POST)  
       
        if form.is_valid():
            user = auth.authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
                LastAuthDate = now()
            )
            test = CustomUser.objects.filter(username=user.get_username)
            messages.error(request, test)
            if user.is_active == False:    
                messages.error(request, 'Вы еще не активированы.') 
            if user.is_active == True:
                auth.login(request, user=user)
                return HttpResponseRedirect(reverse('main'))
        else:
            messages.error(request, 'Ваш аккаунт еще не активирован или вы указали неверные данные!')    

          
        if form_create.is_valid():
            form_create.save()
            messages.success(request, 'Ваша заявка на регистрацию была отправлена, пожалуйста дождитесь пока её одобрят!')
            return HttpResponseRedirect(reverse('login'))

            
    
    return render(request, 'authapp/login.html', context={
        'title': "Вход в систему",
        'form': CustomUserLoginForm(),
        'form_create': CustomUserCreationForm(),
        
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


@login_required
def account(request):
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None

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
        "right":right,
        'userform': userform,
        'userdataform':userdataform
    })

@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None
    userform = CustomUserCreationForm()
    if request.method == 'POST':
        userform = CustomUserCreationForm(data=request.POST)

        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(reverse('all_users'))

    return render(request, 'authapp/create_user.html', context={
        'title': 'Создание аккаунта',
        "right":right,
        'userform': userform
    })