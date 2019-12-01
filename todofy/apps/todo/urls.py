from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='todo_index'),
    path("create/", views.create, name='todo_create'),
    path("<int:todo>/archive/", views.archive, name="todo_archive"),
    path("<int:todo>/delete/", views.delete, name="todo_delete"),
]