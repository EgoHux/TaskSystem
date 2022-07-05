
from django.db import models
from authapp.models import CustomUser
from django.utils import timezone
from django.contrib.auth import get_user_model




class Task(models.Model):

    TASK_TYPE_CHOICES = [
        ("ER", "Ошибка"),
        ("UP", "Обновить"),
        ("RE", "Рекомендация"),
        ("ID", "Идея")

    ]

    STATUS_CHOICES = [
        ("EX", "В ожидании"),
        ("AC", "В производстве"),
        ("MD", "Сделан"),
        ("NI", "Требует доработки")
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, verbose_name="Автор", default=None, related_name='authors')
    executor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Исполнитель", default=None, related_name='executors')
    title = models.CharField("Заголовок", max_length=50, default="")
    description = models.TextField("Описание", max_length=250, default="")
    # files = models.FileField(upload_to="files/", verbose_name="Файлы", default=None, blank=False)
    tasktype = models.CharField(choices=TASK_TYPE_CHOICES, max_length=2, verbose_name="Тип задачи", default="UP")
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, verbose_name="Статус", default="EX")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

