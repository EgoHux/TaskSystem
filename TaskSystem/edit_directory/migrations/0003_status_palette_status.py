# Generated by Django 3.2.9 on 2023-05-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit_directory', '0002_status_next_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='palette_status',
            field=models.CharField(blank=True, default='#000000', help_text='Выберите цветовую палитру', max_length=7, null=True, verbose_name='Цветовая палитра'),
        ),
    ]
