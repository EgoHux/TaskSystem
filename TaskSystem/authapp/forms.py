from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import ValidationError
from .models import CustomUser, UserData

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'is_active')


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'is_active')

        def clean_is_active(self):
            data = self.cleaned_data["is_active"]
            if data == False:
                return ValidationError("Пользователь не активирован!")
            return data


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ('name', 'lastname', 'patronymic', 'birthday', 'gender', 'number', 'email')