from django.db import models
from django.contrib.auth.models import AbstractUser


class Type(models.Model):
    name = models.CharField("Название", blank=True, max_length=40)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    LastAuthDate = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(verbose_name="Пользователь активирован", default=False)



class Right(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    usertype_id = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип пользователя")

    def __str__(self):
        return f"{self.user_id} - {self.usertype_id}"




class UserData(models.Model):
    GENDER_CHOICES = [
        ("M", "Мужской"),
        ("G", "Женский")
    ]

    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", related_name="users", default=None, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Имя", blank=True, max_length=40, null=True)
    lastname = models.CharField(verbose_name="Фамилия", blank=True, max_length=40, null=True)
    patronymic = models.CharField(verbose_name="Отчетсво", blank=True, max_length=40, null=True)
    birthday = models.DateField(verbose_name = "Дата рождения", null=True, blank=True)
    gender = models.CharField(verbose_name="Пол", choices=GENDER_CHOICES, default="", max_length=1, blank=True, null=True)
    number = models.CharField(verbose_name="Номер телефона", blank=True, max_length=11, null=True)
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True)

    def __str__(self):
        return f"{self.lastname} {self.name} {self.patronymic}"