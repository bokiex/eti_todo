from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    content = models.TextField()
    archived = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = 'created_at'