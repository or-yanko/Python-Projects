from django.contrib import admin
from .models import TodoList, Item

# Register your models here.
admin.site.register(TodoList)
admin.site.register(Item)

