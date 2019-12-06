from django.shortcuts import render
from .forms import LoginForm
from .models import User

# Create your views here.
def create(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                password= form.cleaned_data['password']
            )
            item.save()
    return redirect('todo_index')

