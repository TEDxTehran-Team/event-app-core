from django.contrib import admin

from apps.timelines.admin import SectionAdmin

from .models import Speaker, Talk


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['title', 'organizer', 'event']
    search_fields = ['title']
    autocomplete_fields = ['organizer']


class TalkAdmin(admin.ModelAdmin):
    list_display = [
        'section',
        'title',

    ]
    autocomplete_fields = [
        'section',
        'speakers'
    ]


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
