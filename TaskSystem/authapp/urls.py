from django.urls import path
import authapp.views as authapp


app_name = "authapp"

urlpatterns = [

    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('account/', authapp.account, name ='account'),
    path('create_user/', authapp.create_user, name="create_user")
]