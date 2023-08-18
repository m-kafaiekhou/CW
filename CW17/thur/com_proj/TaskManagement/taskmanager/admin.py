from django.contrib import admin
from django.shortcuts import HttpResponse
from .models import Task, Tag, Category, Note
import csv


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_per_page = 20
    list_display = ['title', 'status', 'category']
    actions = ['export_as_csv']
    readonly_fields = ['created_at', 'updated', 'is_active']


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
