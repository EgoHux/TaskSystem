# Generated by Django 3.2.9 on 2022-08-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20220801_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужской'), ('G', 'Женский')], default='', max_length=1, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='lastname',
            field=models.CharField(max_length=40, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='name',
            field=models.CharField(max_length=40, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='number',
            field=models.CharField(max_length=11, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='patronymic',
            field=models.CharField(max_length=40, null=True, verbose_name='Отчетсво'),
        ),
    ]