from django.contrib import admin

from .models import Venue

class VenueAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'organizer'
    ]
    search_fields = [
        'title',
        'organizer__title'
    ]
    autocomplete_fields = ['organizer']


admin.site.register(Venue, VenueAdmin)