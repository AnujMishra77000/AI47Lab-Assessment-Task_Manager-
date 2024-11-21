from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display=['id', 'Task_title', 'Task_description']

  

