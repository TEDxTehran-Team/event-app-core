import graphene

from graphene_django.types import DjangoObjectType

from .models import EventDay, Session, Section


class EventDaySchemaType(DjangoObjectType):
    class Meta:
        model = EventDay


class SessionSchemaType(DjangoObjectType):
    class Meta:
        model = Session

class SectionSchemaType(DjangoObjectType):
    class Meta:
        model = Section


class TimelinesQuery(object):
    pass
