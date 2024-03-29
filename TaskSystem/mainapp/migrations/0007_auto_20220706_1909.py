# Generated by Django 3.2.9 on 2022-07-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20220706_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='color_status',
            field=models.CharField(default='DR', max_length=2, verbose_name='Цвет статуса'),
        ),
        migrations.AddField(
            model_name='status',
            name='comment_is_active',
            field=models.BooleanField(default=False, verbose_name='Возможность комментировать'),
        ),
        migrations.AddField(
            model_name='status',
            name='image_status',
            field=models.ImageField(default=None, upload_to='image_status/', verbose_name='Иконка статуса'),
        ),
        migrations.AddField(
            model_name='status',
            name='name',
            field=models.TextField(default=None, max_length=50, verbose_name='Название статуса'),
        ),
    ]
