# Generated by Django 3.2.9 on 2023-05-03 15:48

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edit_directory', '0003_status_palette_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='palette_status',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None, verbose_name='Палитра статуса'),
        ),
    ]