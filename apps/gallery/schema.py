from event_app.utility import get_organizer
from apps.organizers.models import Organizer
import graphene

from graphene_django.types import DjangoObjectType

from .models import Album, Photo, Video


class AlbumSchemaType(DjangoObjectType):
    class Meta:
        model = Album


class VideoSchema(DjangoObjectType):
    class Meta:
        model = Video

    video_url = graphene.String(description="Video url of the video field")
    thumbnail_url = graphene.String(description="Image url of the thumbnail field")

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

    image_url = graphene.String(description="image url of the image field")
    thumbnail_url = graphene.String(description="image url of the thumbnail field")

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None
    
    def resolve_thumbnail_url(self, info):
        if self.thumbnail:
            return self.thumbnail.url
        return None

class AlbumsQuery(object):
    albums_description = """
    Just like the album query. With only difference that if id is not provided, it will return the list of albums for the organizer.
    """
    albums = graphene.List(AlbumSchemaType, id=graphene.Int(), organizer=graphene.Int(), description = albums_description) 
    album_description = """
    Retrieves Album data of the given id. If organizer is provided, it will search among that organizer's
    talks. Otherwise it will search among the talks of the organizer connected to the application token
    sent by the client.
    """
    album = graphene.Field(AlbumSchemaType, id=graphene.Int(required=True), organizer=graphene.Int(), description=album_description) 

    def resolve_album(self, info, **kwargs):
        organizer_id = get_organizer(info)

        return Album.objects.get(id=kwargs.get('id'),organizer_id=organizer_id)


    def resolve_albums(self, info, **kwargs):
        organizer_id = get_organizer(info)
        id = kwargs.get('id')
        if id:
            return Album.objects.filter(id=kwargs.get('id'),organizer_id=organizer_id).order_by('-id')
        else:
            return Album.objects.filter(organizer_id=organizer_id).order_by('-id')