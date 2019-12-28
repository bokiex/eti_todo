from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def index(request):
    items = Todo.objects.filter(archived=False).order_by('-created_at')
    return render(request, 'todo-index.html', {'items': items, 'form': TodoForm()})


def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            item = Todo(
                content=form.cleaned_data['content'],
                archived=False
            )
            item.save()
    return redirect('todo_index')


def archive(request, todo):
    item = Todo.objects.get(id=todo)
    item.archived = True
    item.save()
    return redirect('todo_index')


def delete(request, todo):
    item = Todo.objects.get(id=todo)
    item.delete()
    return redirect('todo_index')


def history(request):
    items = Todo.objects.order_by('-created_at')
    return render(request, 'todo-history.html', {'items': items})
