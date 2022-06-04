# Register your models here.
from django.contrib import admin
from import_export.admin import ExportActionMixin, ImportExportModelAdmin

from . import models, resources


@admin.register(models.SpeedtesterModel)
class SpeedtesterAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ['best_server', 'download', 'upload', 'created']
    list_filter = ['best_server__country', 'best_server__name', 'best_server__cc']
    search_fields = ['best_server__country', 'best_server__name', 'best_server__cc']
    readonly_fields = ['best_server']
    date_hierarchy = 'created'
    resource_class = resources.SpeedtesterResource


@admin.register(models.ServersModel)
class ServerAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ['url','created', 'name', 'country', 'cc', 'sponsor', 'host']
    list_filter = ['name', 'country', 'cc']
    search_fields = ['name', 'country', 'cc']
    date_hierarchy = 'created'
