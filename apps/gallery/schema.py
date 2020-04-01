import graphene

from graphene_django.types import DjangoObjectType

from .models import Album, Photo, Video


class AlbumSchemaType(DjangoObjectType):
    class Meta:
        model = Album


class VideoSchema(DjangoObjectType):
    class Meta:
        model = Video


class PhotoSchemaType(DjangoObjectType):
    class Meta:
        model = Photo


class AlbumsQuery(object):
    pass
