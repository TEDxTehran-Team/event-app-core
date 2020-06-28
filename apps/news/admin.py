from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'organizer']
    search_fields = ['title']
    autocomplete_fields = ['organizer']

admin.site.register(News, NewsAdmin)