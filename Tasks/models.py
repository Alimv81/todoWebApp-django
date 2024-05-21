from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField(default=datetime.now)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def is_done(self):
        return self.done
