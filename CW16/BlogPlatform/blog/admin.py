from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'datetime_created']
    ordering = ['status']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    ordering = ['name']


admin.site.register(Comment)

