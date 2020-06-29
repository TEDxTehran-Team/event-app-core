import graphene

from graphene_django.types import DjangoObjectType

from .models import Album, Photo, Video


class AlbumSchemaType(DjangoObjectType):
    class Meta:
        model = Album


class VideoSchema(DjangoObjectType):
    class Meta:
        model = Video

    video_url = graphene.String()
    thumbnail_url = graphene.String()

    def resolve_video_url(self, info):
        if self.video:
            return self.video.url
        return None
    
    def resolve_thumbnail_url(self, info):
        if self.thumbnail:
            return self.thumbnail.url
        return None
    

class PhotoSchemaType(DjangoObjectType):
    class Meta:
        model = Photo

    image_url = graphene.String()
    thumbnail_url = graphene.String()

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None
    
    def resolve_thumbnail_url(self, info):
        if self.thumbnail:
            return self.thumbnail.url
        return None

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