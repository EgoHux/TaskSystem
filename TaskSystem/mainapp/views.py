from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "mainapp/login.html", context = {
        "title":"Вход в систему"
    })


def main(request):
    return render(request, 'mainapp/main.html', context={
        "title": "Главное меню"
    })