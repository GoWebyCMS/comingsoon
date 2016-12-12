from django.contrib import admin

from .models import Comingsoon, IgnoreURL

# Customize Models for Admin


class IgnoredURLInline(admin.TabularInline):
    model = IgnoreURL
    extra = 2


class ComingsoonAdmin(admin.ModelAdmin):
    inlines = [IgnoredURLInline]
    list_display = ['__str__', 'active', 'site', 'start', 'end']
    readonly_fields = ('site',)

    #disable actions
    #actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

# Register Models

admin.site.register(Comingsoon, ComingsoonAdmin)
