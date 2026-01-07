from django.urls import path
from . import views

urlpatterns = [
    path("", views.demo),
    path("user/", views.user),
    path("users/", views.users_list),
    path("user/<int:user_id>", views.user_delete)
]