from django.shortcuts import render
from .forms import TodoForm
from .models import Todo


def index(request):
    items = Todo.objects.all()
    return render(request, 'todo-index.html', {'items': items})


def post(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        item = Todo(
            content=form.cleaned_data['content'],
            archived=False
        )
        item.save()

    items = Todo.objects.all()
    return render(request, 'todo-index.html', {'items': items})
