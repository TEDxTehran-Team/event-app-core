import graphene

from graphene_django.types import DjangoObjectType

from .models import Album, Photo, Video


class AlbumSchemaType(DjangoObjectType):
    class Meta:
        model = Album


class VideoSchema(DjangoObjectType):
    class Meta:
        model = Video

    video_url = graphene.String(resolver=lambda  my_obj, resolve_obj: my_obj.image.url)


class PhotoSchemaType(DjangoObjectType):
    class Meta:
        model = Photo

    photo_url = graphene.String(resolver=lambda my_obj, resolve_obj: my_obj.image.url)


class AlbumsQuery(object):
    all_album = graphene.List(AlbumSchemaType)
    album = graphene.Field(AlbumSchemaType, id=graphene.Int(required=True))
    album_by_organizer = graphene.List(AlbumSchemaType, organizer=graphene.Int(required=True))

    def resolve_all_album(self, info, **kwargs):
        return Album.objects.all()

    def resolve_album(self, info, **kwargs):
        return Album.objects.get(id=kwargs.get('id'))

    def resolve_album_by_organizer(self, info, **kwargs):
        id = kwargs.get('organizer')
        return Album.objects.filter(organizer__id=id)