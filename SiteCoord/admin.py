from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Sites

@admin.register(Sites)
class SiteAdmin(ImportExportModelAdmin):
    list_display = ("SiteID", "SiteName", "SiteManager", "SiteEngineer", "Longitude", "Latitude")
    pass
