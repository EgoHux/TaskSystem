from dataclasses import fields
from django import forms

from .models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("author", "executor", "title", "description", "files", "tasktype", "status",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "author":
                field.widget = forms.HiddenInput()



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", "files")
                    




