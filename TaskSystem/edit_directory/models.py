from django.db import models


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
    image_status = models.ImageField(verbose_name="Иконка статуса", upload_to='image_status/', default=None, blank=True)

    def __str__(self):
        return self.name

class TaskType(models.Model):
    name = models.CharField(max_length=30, verbose_name="Тип заявки")

    def __str__(self):
        return f"{self.name}"