from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items = Todo.objects.filter(user=request.user, archived=False).order_by('-created_at')
    return render(request, 'todo-index.html', {'items': items, 'form': TodoForm()})


@login_required
def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            item = Todo(
                content=form.cleaned_data['content'],
                archived=False,
                user=request.user
            )
            item.save()
    return redirect('todo_index')


@login_required
def archive(request, todo):
    item = Todo.objects.get(id=todo)
    item.archived = True
    item.save()
    return redirect('todo_index')


@login_required
def delete(request, todo):
    item = Todo.objects.get(id=todo)
    item.delete()
    return redirect('todo_index')


@login_required
def history(request):
    items = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo-history.html', {'items': items})
