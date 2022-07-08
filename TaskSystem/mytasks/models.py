from django.db import models
from django.contrib.auth import get_user_model
from mainapp.models import Task


class MyTask(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='mytask', verbose_name="Пользователь")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task}"