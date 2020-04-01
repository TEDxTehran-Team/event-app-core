from django.contrib import admin

from apps.timelines.admin import EventDayInline
from .models import EventType, Event, EventLink, AboutEvent


class EventTypeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'organizer'
    ]
    list_filter = ['organizer']
    search_fields = ['title']
    autocomplete_fields = ['organizer']


class AboutEventInline(admin.StackedInline):
    model = AboutEvent
    extra = 1


class EventLinkInline(admin.TabularInline):
    model = EventLink
    extra = 1


class EventAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'organizer',
        'event_type'
    ]
    search_fields = ['title']
    list_filter = [
        'organizer',
        'event_type'
    ]
    autocomplete_fields = [
        'organizer',
        'event_type',
        'venue'
    ]
    inlines = [
        EventLinkInline,
        EventDayInline,
        AboutEventInline
    ]


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
