from django.urls import path
import edit_directory.views as edit_directory


app_name = "edit_directory"

urlpatterns = [

    path("", edit_directory.view, name='view'),
    path("edit_status/<int:status_id>", edit_directory.edit_status, name='edit_status'),
    path('edit_tasktype/<int:tasktype_id>', edit_directory.edit_tasktype, name='edit_tasktype')
]