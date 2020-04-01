import graphene

from graphene_django.types import DjangoObjectType

from .models import Talk, Speaker


class SpeakerSchema(DjangoObjectType):
    class Meta:
        model = Speaker


class TalkSchemaType(DjangoObjectType):
    class Meta:
        model = Talk


class TalksQuery(object):
    pass
