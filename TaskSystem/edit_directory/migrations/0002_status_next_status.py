# Generated by Django 3.2.9 on 2023-04-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit_directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='next_status',
            field=models.ManyToManyField(blank=True, related_name='_edit_directory_status_next_status_+', to='edit_directory.Status'),
        ),
    ]
