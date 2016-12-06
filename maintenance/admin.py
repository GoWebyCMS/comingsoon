from django.contrib import admin

# Register your models here.
from .models import Maintenance, IgnoredURL


class IgnoredURLInline(admin.TabularInline):
    model = IgnoredURL
    extra = 2


class MaintenanceAdmin(admin.ModelAdmin):
    inlines = [IgnoredURLInline, ]
    list_display = ['__str__', 'active']
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return True

admin.site.register(Maintenance, MaintenanceAdmin)
