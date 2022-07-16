from django.shortcuts import render
from django.urls import reverse
from edit_directory.models import Status, TaskType
from edit_directory.forms import StatusForm, TaskTypeForm
from django.http.response import HttpResponseRedirect


# Create your views here.
def view(request):
    status = Status.objects.all()
    tasktype = TaskType.objects.all()
    return render(request, 'edit_directory/edit_directory.html', context={
        'title': "Редактирование справочников",
        'statuses':status,
        'tasktypes': tasktype

    })

def edit_status(request, status_id):
    status=Status.objects.get(id=status_id)
    form = StatusForm(instance=status)
    if request.method == "POST":
        form = StatusForm(data=request.POST, instance=status)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('view'))

    return render(request, 'edit_directory/edit_status.html', context={
        'form': form
    })

def edit_tasktype(request, tasktype_id):
    tasktype = TaskType.objects.get(id=tasktype_id)
    form = TaskTypeForm(instance=tasktype)
    if request.method == "POST":
        form = TaskTypeForm(data=request.POST, instance=tasktype)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('view'))

    return render(request, 'edit_directory/edit_tasktype.html', context={
        'form': form
    })

