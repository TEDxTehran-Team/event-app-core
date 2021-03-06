from django.contrib import admin

from .models import Organizer, OrganizerAccount, AboutOrganizer


class OrganizerAccountInline(admin.TabularInline):
    model = OrganizerAccount
    extra = 1
    autocomplete_fields = ['user']


class AboutOrganizerInline(admin.StackedInline):
    model = AboutOrganizer
    extra = 1


class OrganizerAdmin(admin.ModelAdmin):
    list_display = ['title', 'has_active_event']
    search_fields = [
        'title',
        'slug'
    ]
    autocomplete_fields = ['main_event']
    
    inlines = [
        OrganizerAccountInline,
        AboutOrganizerInline
    ]


admin.site.register(Organizer, OrganizerAdmin)
