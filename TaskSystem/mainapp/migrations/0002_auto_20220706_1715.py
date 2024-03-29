# Generated by Django 3.2.9 on 2022-07-06 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='', max_length=250, verbose_name='Описание')),
                ('files', models.FileField(default=None, upload_to='files/', verbose_name='Файлы')),
                ('tasktype', models.CharField(choices=[('ER', 'Ошибка'), ('UP', 'Предложение'), ('OT', 'Другое')], default='UP', max_length=2, verbose_name='Тип задачи')),
                ('status', models.CharField(choices=[('EX', 'В ожидании'), ('AC', 'В производстве'), ('MD', 'Сделан'), ('NI', 'Требует доработки'), ('FL', 'Отклонен')], default='EX', max_length=2, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('executor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='executors', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
            ],
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
