from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'organizer',
        'event'
    ]
    search_fields = [
        'title',
        'organizer__title',
        'event__title'
    ]
    autocomplete_fields = [
        'organizer',
        'event'
    ]


admin.site.register(News, NewsAdmin)