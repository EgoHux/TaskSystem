# Generated by Django 3.2.9 on 2022-08-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, max_length=100, verbose_name='Текст'),
        ),
    ]