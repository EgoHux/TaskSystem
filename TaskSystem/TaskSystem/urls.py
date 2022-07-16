"""TaskSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static
from authapp import views as authapp
from edit_directory import views as edit_directory



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authapp.login, name="login"),
    path('main', mainapp.main, name ='main'),
    path('create', mainapp.create_task, name='create'),
    path("auth/", include('authapp.urls', namespace="auth")),
    path('tasks/', include('mytasks.urls', namespace='tasks')),
    path('edit_directory/', include('edit_directory.urls', namespace='edit_directory'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)