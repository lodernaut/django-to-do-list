# Register your models here.
from django.contrib import admin

from todoAPP.models import ToDoItem, ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    pass


admin.site.register(ToDoList, ToDoListAdmin)


class ToDoItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(ToDoItem, ToDoItemAdmin)
