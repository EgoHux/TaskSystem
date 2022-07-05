from django.shortcuts import render
from .models import Task
# Create your views here.



def main(request):
    tasks = Task.objects.all()
    return render(request, 'mainapp/main.html', context={
        "title": "Главное меню",
        "tasks": tasks
    })