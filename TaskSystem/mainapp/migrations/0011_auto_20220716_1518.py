# Generated by Django 3.2.9 on 2022-07-16 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_task_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='image_status',
            field=models.ImageField(blank=True, default=None, upload_to='image_status/', verbose_name='Иконка статуса'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.status', verbose_name='Статус'),
        ),
    ]
