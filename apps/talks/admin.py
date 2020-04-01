from django.contrib import admin

from apps.timelines.admin import SectionAdmin

from .models import Speaker, Talk

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['title', 'organizer']
    search_fields = ['title']
    autocomplete_fields = ['organizer']


class TalkAdmin(SectionAdmin):
    list_display = [
        'title',
        'session'
    ]
    autocomplete_fields = [
        'session',
        'speakers'
    ]
    exclude = ['type']


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
