from django.contrib import admin
from authapp.models import Right, Type, UserData
from .models import Task, Comment, Status, TaskType

# Register your models here.
admin.site.register(Right)
admin.site.register(Type)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Status)
admin.site.register(UserData)
admin.site.register(TaskType)