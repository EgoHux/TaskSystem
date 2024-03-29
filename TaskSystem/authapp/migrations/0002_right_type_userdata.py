# Generated by Django 3.2.9 on 2022-07-06 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=40, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=40, verbose_name='Отчетсво')),
                ('birthday', models.DateField(null=True, verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('G', 'Женский')], default=None, max_length=1, verbose_name='Пол')),
                ('number', models.CharField(blank=True, max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('usertype_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authapp.type', verbose_name='Тип пользователя')),
            ],
        ),
    ]
