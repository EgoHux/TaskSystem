# Generated by Django 3.2.9 on 2022-07-30 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_userdata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='right',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='right',
            name='usertype_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.type', verbose_name='Тип пользователя'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
