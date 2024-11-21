from django.db import models
from django.contrib.auth.models import User

#model to store Task details title and there descriptions
class Task(models.Model):
    Task_title = models.CharField(max_length=100)
    Task_description = models.TextField()

