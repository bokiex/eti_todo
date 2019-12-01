from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='todo_index'),
    path("create/", views.post, name='todo_create'),
]
