from django.db import models
from django.contrib.auth.models import AbstractUser


class Type(models.Model):
    name = models.CharField("Название", blank=True, max_length=40)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    LastAuthDate = models.DateField(auto_now=True)
    name = models.CharField(blank=True, max_length=40)
    lastname = models.CharField(blank=True, max_length=40)
    patronymic = models.CharField(blank=True, max_length=40)
    number = models.CharField(blank=True, max_length=11)
    email = models.EmailField(blank=True)



class Right(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Пользователь")
    usertype_id = models.ForeignKey( Type, on_delete=models.DO_NOTHING, verbose_name="Тип пользователя")

    def __str__(self):
        return f"{self.user_id} - {self.usertype_id}"




# class UserData(models.Model):
#     user_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='userdata_id')
#     name = models.CharField(blank=True, max_length=40)
#     lastname = models.CharField(blank=True, max_length=40)
#     patronymic = models.CharField(blank=True, max_length=40)
#     number = models.CharField(blank=True, max_length=11)
#     email = models.EmailField(blank=True)