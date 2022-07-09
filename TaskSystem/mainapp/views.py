from django.shortcuts import render, redirect
from .models import Task, Comment
from .forms import TaskForm
# Create your views here.



def main(request):
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