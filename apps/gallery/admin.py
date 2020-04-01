from django.contrib import admin

from .models import Album, Photo, Video


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class VideoInline(admin.StackedInline):
    model = Video
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
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
    inlines = [
        PhotoInline,
        VideoInline
    ]


admin.site.register(Album, AlbumAdmin)
