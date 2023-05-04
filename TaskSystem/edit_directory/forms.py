from django import forms
from colorfield.widgets import ColorWidget
from edit_directory.models import Status, TaskType
from django.forms.widgets import TextInput


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name', 'comment_is_active', 'color_status', 'image_status')
        widgets = {
            'color_status': TextInput(attrs={'type': 'color'}),
        }

    
class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ('name',)