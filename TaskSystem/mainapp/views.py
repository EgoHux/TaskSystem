from django.db.models import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from .models import Task, Comment
from .forms import TaskForm
from authapp.models import CustomUser, UserData
from authapp.forms import CustomUserChangeForm, UserDataForm
from django.utils.timezone import now
# Create your views here.



def main(request):
    CustomUser.objects.filter(pk=request.user.pk).update(LastAuthDate=now())
    tasks = Task.objects.all()
    comments = Comment.objects.all()
    return render(request, 'mainapp/main.html', context={
        "title": "Главное меню",
        "tasks": tasks,
        "comments": comments
    })

def create_task(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = "Ошибка заполнения задачи"

    return render(request, 'mainapp/create.html', context={
        'title':"Создать задачу",
        'form': TaskForm(),
        'error': error
    })

def all_users(request):
    users = CustomUser.objects.all()

    usersdata = UserData.objects.all()
    non_active_user = CustomUser.objects.filter(is_active=False)
    return render(request, 'mainapp/all_users.html', context={
        'title':"Все пользователи",
        'users': users,
        'userdata': usersdata,
        'non_active_user': non_active_user

    })

def edit_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)

    try:
        userdata = UserData.objects.get(user=user_id)
    except:
        userdata = UserData.objects.create(user=user, gender="M")

    userform = CustomUserChangeForm(instance=user)
    userdataform = UserDataForm(instance=userdata)

    if request.method =='POST':

        userform = CustomUserChangeForm(instance=user, data=request.POST)
        userdataform = UserDataForm(data=request.POST, instance=userdata)

        if userform.is_valid() and userdataform.is_valid():
            userform.save()

            userdataform.save()

            return HttpResponseRedirect(reverse('all_users'))

    return render(request, 'mainapp/edit_user.html', context={
        'title':'Изменить пользователя',
        'userform':userform,
        'userdataform': userdataform
    })

def delete_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    #userdata = get_object_or_404(UserData, user=user_id)
    user.delete()
    #userdata.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))