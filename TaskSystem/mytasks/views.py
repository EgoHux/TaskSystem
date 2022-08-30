from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from edit_directory.models import Status
from .models import MyTask
from mainapp.models import Task, Comment
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from authapp.models import Right
# Create your views here.

@login_required
def view(request):
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None
    return render(request, 'mytasks/base.html', context={
        'title':"Мои задачи",
        'mytasks': MyTask.objects.filter(user=request.user),
        "right":right,
        "comments": Comment.objects.all()

    })

@login_required
def add(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    mytask = MyTask.objects.filter(user=request.user, task=task)
    if task.executor == None:
        task.executor = request.user
    if task.status.name == "В ожидании":
        task.status = Status.objects.get(id=2)
    task.save()
    # task.status.name = Status.objects.get(name="В разработке")
    # task.save()
    
    if mytask:
        mytask_item = mytask[0]
        mytask_item.save()
    else:
        mytask_item = MyTask(user=request.user, task=task)
        mytask_item.save()
      

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse("main")))

@login_required
def delete(request, mytask_id):
    mytask = get_object_or_404(MyTask, pk=mytask_id)
    mytask.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def complete(request, mytask_id):
    mytask = get_object_or_404(MyTask, pk=mytask_id)
    task = get_object_or_404(Task, pk=mytask.task.id)
    task.status = Status.objects.get(id=3)
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))