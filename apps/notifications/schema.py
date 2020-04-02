import graphene

from graphene_django.types import DjangoObjectType

from .models import News


class NewsSchemaType(DjangoObjectType):
    class Meta:
        model = News


class NotificationsQuery(object):
    pass
