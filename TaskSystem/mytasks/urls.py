from django.urls import path
import mytasks.views as mytasks


app_name = "mytasks"

urlpatterns = [

    path('', mytasks.view, name='view'),
    path('add/<int:task_id>', mytasks.add, name='add'),
    path('delete/<int:mytask_id>', mytasks.delete, name='delete')


]