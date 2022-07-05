from django.contrib import admin
from authapp.models import Right, Type
from .models import Task
# Register your models here.
admin.site.register(Right)
admin.site.register(Type)
admin.site.register(Task)