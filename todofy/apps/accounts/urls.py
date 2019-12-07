from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
  url('', include('django.contrib.auth.urls'), name='login_index'),
]