from django.contrib import admin
from .models import CustomUser




@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [ 'username', 'name', 'lastname', 'patronymic', 'email', 'number' ]
    fields = ('username', 'password', 'email', 'number', 'name', 'lastname', 'patronymic')




