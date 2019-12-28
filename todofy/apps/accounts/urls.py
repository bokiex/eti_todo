from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
  url('', include('django.contrib.auth.urls'), name='login_index'),
  path('signup/', views.SignUp.as_view(), name='signup'),
]