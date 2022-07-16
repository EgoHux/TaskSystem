from django import forms

from edit_directory.models import Status, TaskType


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name', 'comment_is_active', 'color_status', 'image_status')


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ('name',)