from django.shortcuts import render

# Create your views here.


def view(request):
    return render(request, 'mytasks/base.html', context={
        'title':"Мои задачи",

    })


def add(request):
    pass


def delete(request):
    pass