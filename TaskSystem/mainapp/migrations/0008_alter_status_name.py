# Generated by Django 3.2.9 on 2022-07-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20220706_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(default=None, max_length=50, verbose_name='Название статуса'),
        ),
    ]
