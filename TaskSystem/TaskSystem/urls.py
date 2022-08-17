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




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authapp.login, name="login"),
    path('main', mainapp.main, name ='main'),
    path('all_users', mainapp.all_users, name="all_users"),
    path('all_users/edit_user/<int:user_id>/', mainapp.edit_user, name='edit_user'),
    path('create', mainapp.create_task, name='create'),
    path("auth/", include('authapp.urls', namespace="auth")),
    path('tasks/', include('mytasks.urls', namespace='tasks')),
    path('creation_tasks/', mainapp.creation_tasks, name="creation_tasks"),
    path('creation_tasks/edit/<int:pk>', mainapp.edit_creation_tasks, name="edit_creation_tasks"),
    path('creation_tasks/delete/<int:pk>', mainapp.creation_tasks_delete, name='creation_tasks_delete'),
    path('edit_directory/', include('edit_directory.urls', namespace='edit_directory')),
    path('delete/<int:user_id>', mainapp.delete_user, name='delete_user')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)