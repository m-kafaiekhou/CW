from django.contrib import admin
from .models import CustomUser
from taskmanager.models import Task
from django.db.models import Count

# Register your models here.


class UserGreatFilter(admin.SimpleListFilter):
    title = "is Great"
    parameter_name = "great"

    def lookups(self, request, model_admin):
        return [
            ("great", "Is Great"),
            ("not_great", "Not Great"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "great":
            return queryset.distinct().filter(number_of_tasks__gt=10)

        if self.value():
            return queryset.distinct().filter(number_of_tasks__lte=10)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(number_of_tasks=Count('task'))
        return qs

    def number_of_tasks(self, obj):
        return obj.number_of_tasks

    list_display = ['username', 'email', 'is_staff', 'number_of_tasks']
    number_of_tasks.admin_order_field = 'number_of_tasks'
    list_filter = (UserGreatFilter, )



