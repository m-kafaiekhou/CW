from django.contrib import admin
from .models import CustomUser
from taskmanager.models import Task
from django.db.models import Count

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     qs.annotate(num=Count('task'))
    #     return qs

    def number_of_tasks(self, obj):
        num = obj.task_set.count()
        return num

    list_display = ['username', 'email', 'is_staff', 'number_of_tasks']
    # ordering = ['number_of_tasks']
    number_of_tasks.admin_order_field = 'customuser_task_count'
    # sortable_by = ['number_of_tasks']


