from django.urls import path
import edit_directory.views as edit_directory


app_name = "edit_directory"

urlpatterns = [

    path("", edit_directory.view, name='directory_view'),
    path("create_status", edit_directory.create_status, name='create_status'),
    path("edit_status/<int:status_id>", edit_directory.edit_status, name='edit_status'),
    path('delete_status/<int:pk>', edit_directory.delete_status, name="delete_status"),
    path("create_tasktype", edit_directory.create_tasktype, name='create_tasktype'),
    path('edit_tasktype/<int:tasktype_id>', edit_directory.edit_tasktype, name='edit_tasktype'),
    path('delete_tasktype/<int:pk>', edit_directory.delete_tasktype, name="delete_tasktype"),
]