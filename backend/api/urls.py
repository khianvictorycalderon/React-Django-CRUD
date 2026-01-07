from django.urls import path
from . import views

urlpatterns = [
    path("", views.demo),
    path("user/", views.user),                     
    path("users/", views.users_list),             
    path("user/<int:user_id>/update/", views.user_update),
    path("user/<int:user_id>/delete/", views.user_delete),
]