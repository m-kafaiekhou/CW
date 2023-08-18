from django.contrib import admin
from .models import Task, Tag, Category, Note

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'status', 'category']

    readonly_fields = ['created_at', 'updated']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_per_page = 20
