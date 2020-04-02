import graphene

from graphene_django.types import DjangoObjectType

from .models import Event, EventLink, EventType, AboutEvent


class EventSchemaType(DjangoObjectType):
    class Meta:
        model = Event


class EventTypeSchema(DjangoObjectType):
    class Meta:
        model = EventType


class EventLinkSchemaType(DjangoObjectType):
    class Meta:
        model = EventLink


class AboutEventSchemaType(DjangoObjectType):
    class Meta:
        model = AboutEvent


class EventsQuery(object):
    pass
