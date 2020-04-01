from django.contrib import admin

from .models import Application, ApplicationToken


class ApplicationTokenInline(admin.TabularInline):
    model = ApplicationToken
    readonly_fields = ['key']
    can_delete = True

    def has_add_permission(self, *args, **kwargs):
        return False


class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'organizer'
    ]
    search_fields = [
        'title',
        'organizer__title',
        'slug'
    ]
    inlines = [ApplicationTokenInline]
    autocomplete_fields = ['organizer']


class ApplicationTokenAdmin(admin.ModelAdmin):
    list_display = [
        'application',
        'key',
        'active'
    ]
    list_filter = ['active']
    readonly_fields = [
        'created_at',
        'key'
    ]
    search_fields = [
        'application__title',
        'application__slug',
        'key'
    ]
    autocomplete_fields = ['application']

admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationToken, ApplicationTokenAdmin)
