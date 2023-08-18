from django.contrib import admin
from django.shortcuts import HttpResponse
from .models import Task, Tag, Category, Note
import csv
import json
from django.http import JsonResponse


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


class ExportJsonMixin:
    def export_as_json(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        j = {}

        for i, obj in enumerate(queryset):
            row = {field: getattr(obj, field).__str__() for field in field_names}
            j[i] = row

        response = JsonResponse(j, content_type='text/json')
        response['Content-Disposition'] = 'attachment; filename={}.json'.format(meta)

        return response

    export_as_json.short_description = "Export Json"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin, ExportCsvMixin, ExportJsonMixin):
    list_per_page = 20
    list_display = ['title', 'status', 'category']
    actions = ['export_as_csv', 'export_as_json']
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
