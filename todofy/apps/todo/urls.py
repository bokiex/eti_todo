from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='todo_index'),
    path("history/", views.history, name='todo_history'),
    path("create/", views.create, name='todo_create'),
    path("<int:todo>/archive/", views.archive, name="todo_archive"),
    path("<int:todo>/delete/", views.delete, name="todo_delete"),
]