from django.db import models

# Create your models here.
# todos/models.py
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(default='Unstarted', max_length=100)

    def __str__(self):
        """A string representation of the model."""
        return self.title