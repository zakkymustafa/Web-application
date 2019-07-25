from django.urls import path
from .views import register_user
from .views import login_user
from .views import list_users
from .views import edit_user

urlpatterns=[
   path("register/",register_user,name="register_user"),
   path("login/",login_user,name="login_user"),
   path("list/",list_users,name="list_user"),
   path("edit/<int:pk>/",edit_user,name="edit_user"),
   

]