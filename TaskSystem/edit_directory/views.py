from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from edit_directory.models import Status, TaskType
from edit_directory.forms import StatusForm, TaskTypeForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from authapp.models import Right


# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def view(request):
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None
    status = Status.objects.all()
    tasktype = TaskType.objects.all()
    return render(request, 'edit_directory/edit_directory.html', context={
        'title': "Редактирование справочников",
        'statuses':status,
        "right":right,
        'tasktypes': tasktype

    })


@user_passes_test(lambda u: u.is_superuser)
def create_status(request):
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None
    form = StatusForm()
    if request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('edit_directory:directory_view'))
    return render(request, 'edit_directory/create_status.html', context={
        'title':"Создание статуса",
        "right":right,
        'form':form
    })


@user_passes_test(lambda u: u.is_superuser)
def edit_status(request, status_id):
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None
    status=Status.objects.get(id=status_id)
    form = StatusForm(instance=status)
    if request.method == "POST":
        form = StatusForm(data=request.POST, instance=status)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('edit_directory:directory_view'))

    return render(request, 'edit_directory/edit_status.html', context={
        "right":right,
        'form': form
    })


@user_passes_test(lambda u: u.is_superuser)
def create_tasktype(request):
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None
    form = TaskTypeForm()
    if request.method == 'POST':
        form = TaskTypeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('edit_directory:directory_view'))
    return render(request, 'edit_directory/create_tasktype.html', context={
        'title':"Создание типа заявки",
        "right":right,
        'form':form
    })


@user_passes_test(lambda u: u.is_superuser)
def edit_tasktype(request, tasktype_id):
    try:
        right = Right.objects.get(user_id=request.user)
    except:
        right = None
    tasktype = TaskType.objects.get(id=tasktype_id)
    form = TaskTypeForm(instance=tasktype)
    if request.method == "POST":
        form = TaskTypeForm(data=request.POST, instance=tasktype)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('edit_directory:directory_view'))

    return render(request, 'edit_directory/edit_tasktype.html', context={
        'form': form,
        "right":right,
    })


@user_passes_test(lambda u: u.is_superuser)
def delete_status(request, pk):
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return HttpResponseRedirect(reverse("edit_directory:directory_view"))



@user_passes_test(lambda u: u.is_superuser)
def delete_tasktype(request, pk):
    tasktype = get_object_or_404(TaskType, pk=pk)
    tasktype.delete()
    return HttpResponseRedirect(reverse("edit_directory:directory_view"))
