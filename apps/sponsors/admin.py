from django.contrib import admin

from .models import Sponsors, SponsorsType


class SponsorsAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    search_fields = ['title']
    list_filter = ['type']


class SponsorTypesAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


admin.site.register(SponsorsType, SponsorTypesAdmin)
admin.site.register(Sponsors, SponsorsAdmin)
