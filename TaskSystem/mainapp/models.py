
from django.db import models
from authapp.models import CustomUser
from django.utils import timezone
from django.contrib.auth import get_user_model




class Task(models.Model):

    TASK_TYPE_CHOICES = [
        ("ER", "Ошибка"),
        ("UP", "Предложение"),
        ("OT", "Другое")


    ]

    STATUS_CHOICES = [
        ("EX", "В ожидании"),
        ("AC", "В производстве"),
        ("MD", "Сделан"),
        ("NI", "Требует доработки"),
        ("FL", "Отклонен")

    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, verbose_name="Автор", default=get_user_model(), related_name='authors')
    executor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Исполнитель", default=None, related_name='executors')
    description = models.TextField("Описание", max_length=250, default="")
    files = models.FileField(upload_to="files/", verbose_name="Файлы", blank=True, default=None)
    tasktype = models.CharField(choices=TASK_TYPE_CHOICES, max_length=2, verbose_name="Тип задачи", default="UP")
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, verbose_name="Статус", default="EX")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.description


class HistoryTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, verbose_name="Задача", default=None, related_name='task')
    #Придумать реализацию сохранения старой инфы
    #Отображение новой инфы
    change = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, verbose_name="Задача", default=None, related_name='сomments')
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, verbose_name="Автор", default=None)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="Текст", max_length=100)
    files = models.FileField(upload_to="comment_files/", verbose_name="Прикрепленные файлы", blank=True, default=None)

    def __str__(self):
        return f"{self.author}: {self.text}"



class Status(models.Model):
    COLOR_CHOICES = [
        ("GR", "Зеленый"),
        ("RD", "Красный"),
        ("YE", "Желтый"),
        ("DR", "Серый")
    ]
    name = models.CharField(verbose_name="Название статуса", max_length=50, default=None)
    comment_is_active = models.BooleanField(verbose_name="Возможность комментировать", default=False)
    color_status = models.CharField(verbose_name="Цвет статуса", choices=COLOR_CHOICES, max_length=2, default= "DR")
    image_status = models.ImageField(verbose_name="Иконка статуса", upload_to='image_status/', default=None)

    def __str__(self):
        return self.name