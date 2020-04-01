from django.contrib import admin

from .models import EventType, Event, AboutEvent


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
    model = Event.links.through
    extra = 1
    # todo add form to accept data here


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
        'event_type'
        # Todo add venue
    ]
    inlines = [
        EventLinkInline,
        AboutEventInline
    ]



admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
