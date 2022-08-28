
from turtle import right
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from .models import Task, Comment
from .forms import TaskForm, CommentForm
from authapp.models import CustomUser, UserData, Right
from authapp.forms import CustomUserChangeForm, UserDataForm
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


@login_required
def main(request):
    CustomUser.objects.filter(pk=request.user.pk).update(LastAuthDate=now())
    tasks = Task.objects.all()
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None
    return render(request, 'mainapp/main.html', context={
        "title": "Главное меню",
        "tasks": tasks,
        "right":right
    })


@login_required
def task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comment = Comment.objects.filter(task=task)
    form = CommentForm()
    if request.method =="POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.data = now
            form.author = request.user
            form.task = task
            form.save()
            return HttpResponseRedirect(reverse('task', args=[pk]))
    return render(request, 'mainapp/task.html', context={
        "title": f"Задача №{task.id}",
        'task':task,
        'comments':comment,
        'form':form
    })

@login_required
def create_task(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    form = TaskForm()
    # form.author = user
    if request.method == "POST":
        form = TaskForm(data=request.POST)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.author = user
            form.save()
            return HttpResponseRedirect(reverse('main'))

    return render(request, 'mainapp/create.html', context={
        'title':"Создать задачу",
        'form': form
    })

@login_required
def creation_tasks(request):
    task=Task.objects.filter(author=request.user)
    return render(request, 'mainapp/creation_tasks.html', context={
        'title':"Созданные задачи",
        'tasks':task
    })

@login_required
def edit_creation_tasks(request, pk):
    task=get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("creation_tasks"))
    return render(request, 'mainapp/edit_creation_tasks.html', context={
        'title':"Созданные задачи",
        'task':task,
        'form':form
    })

@login_required
def creation_tasks_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse('creation_tasks'))

@user_passes_test(lambda u: u.is_superuser)
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



@user_passes_test(lambda u: u.is_superuser)
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
        'user':user,
        'userform':userform,
        'userdataform': userdataform
    })


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    #userdata = get_object_or_404(UserData, user=user_id)
    user.delete()
    #userdata.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))