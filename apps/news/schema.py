from apps.organizers.models import Organizer
import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import News

class NewsSchemaType(DjangoObjectType):
    class Meta:
        model = News
    
    icon_url = graphene.String()
    def resolve_icon_url(self, info):
        if self.icon:
            return self.icon.url
        return None

class NewsQuery(object):
    news = graphene.List(NewsSchemaType, organzier=graphene.Int(required=False), id=graphene.Int(required=False))

    def resolve_news(self, info, **kwargs):
        organizer_id = kwargs.get('organizer')
        if not organizer_id:
            organizer_id = Organizer.objects.first().id

        id = kwargs.get('id')
        if id:
            return News.objects.filter(organizer_id=organizer_id, id=id)
        else:
            return News.objects.filter(organizer_id=organizer_id)
