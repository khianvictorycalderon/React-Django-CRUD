from django.urls import path
from . import views

urlpatterns = [
    path("", views.demo),
    path("user/", views.user)
]