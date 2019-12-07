from django.shortcuts import render
from .forms import LoginForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('todo_index')
        # Redirect to a success page.
    else:
        return "Invalid login"

def logout(request):
    logout(request)
    return redirect('login_index')