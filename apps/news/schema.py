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
    all_news = graphene.List(NewsSchemaType)
    news_by_organizer = graphene.List(NewsSchemaType, organizer=graphene.Int(required=True))

    def resolve_all_news(self, info):
        return News.objects.all()
    
    def resolve_news_by_organizer(self, info, **kwargs):
        id = kwargs.get('organizer')
        return News.objects.filter(organizer_id=id)
    