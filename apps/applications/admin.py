from django.contrib import admin

from .models import Application, ApplicationToken


class ApplicationTokenInline(admin.TabularInline):
    model = ApplicationToken
    extra = 0
    readonly_fields = ['key']
    can_delete = True


class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'organizer'
    ]
    list_filter = []
    readonly_fields = []
    filter_horizontal = []
    search_fields = [
        'title',
        'organizer__title',
        'slug'
    ]
    exclude = []
    inlines = [ApplicationTokenInline]


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
    filter_horizontal = []
    search_fields = [
        'application__title',
        'application__slug',
        'key'
    ]
    exclude = []


admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationToken, ApplicationTokenAdmin)
