from event_app.utility import get_organizer
from apps.organizers.models import Organizer
import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import News

class NewsSchemaType(DjangoObjectType):
    class Meta:
        model = News
    
    icon_url = graphene.String(description="Image url for icon field")
    image_url = graphene.String(description="Image url for image field")

    def resolve_icon_url(self, info):
        if self.icon:
            return self.icon.url
        return None

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None

class NewsQuery(object):
    news_description="""
    This query returns the news object of id is provided. If organizer id is provided, it will return the list of news objects for that organizer.
    If organizer id is not provided, It will return the list of news corresponding to the organizer connected to the application token provided 
    by the client.
    """
    news = graphene.List(NewsSchemaType, organzier=graphene.Int(required=False), id=graphene.Int(required=False), description=news_description)

    def resolve_news(self, info, **kwargs):
        organizer_id = get_organizer(info)
        id = kwargs.get('id')
        if id:
            return News.objects.filter(organizer_id=organizer_id, id=id)
        else:
            return News.objects.filter(organizer_id=organizer_id)
