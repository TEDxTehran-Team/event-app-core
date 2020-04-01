from django.contrib import admin

from .models import EventDay, Session, Section


class EventDayInline(admin.StackedInline):
    model = EventDay
    extra = 1


class SessionInline(admin.StackedInline):
    model = Session
    extra = 1


class SectionInline(admin.StackedInline):
    model = Section
    extra = 1
    exclude = ['ordering']


class EventDayAdmin(admin.ModelAdmin):
    list_display = [
        'event',
        'date'
    ]
    date_hierarchy = 'date'
    search_fields = [
        'title',
        'event__title'
    ]
    inlines = [SessionInline]
    autocomplete_fields = ['event']


class SessionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'day',
        'start_time',
        'end_time'
    ]
    search_fields = [
        'title',
        'day__title'
    ]
    inlines = [SectionInline]
    autocomplete_fields = ['day']


class SectionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'session',
        'type',
        'start_time',
        'end_time'
    ]
    search_fields = [
        'title',
        'session__title'
    ]
    list_filter = [
        'type'
    ]
    autocomplete_fields = ['session']


admin.site.register(EventDay, EventDayAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Section, SectionAdmin)
