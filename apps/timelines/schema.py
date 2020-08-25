import graphene

from graphene_django.types import DjangoObjectType

from .models import EventDay, Session, Section


class EventDaySchemaType(DjangoObjectType):
    class Meta:
        model = EventDay


class SessionSchemaType(DjangoObjectType):
    class Meta:
        model = Session

    image_url = graphene.String()

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None

class SectionSchemaType(DjangoObjectType):
    class Meta:
        model = Section

    image_url = graphene.String()
    cover_url = graphene.String()

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None
    
    def resolve_cover_url(self, info):
        if self.cover:
            return self.cover.url
        return None


class TimelinesQuery(object):

    event_day = graphene.Field(EventDaySchemaType, id=graphene.Int(), event=graphene.Int())
    session = graphene.Field(SessionSchemaType, id=graphene.Int(required=True))
    section = graphene.Field(SectionSchemaType, id=graphene.Int(required=True))

    def resolve_session(self, info, **kwargs):
        return Session.objects.get(id=kwargs.get('id'))

    def resolve_section(self, info, **kwargs):
        return Session.objects.get(id=kwargs.get('id'))

    def resolve_event_day(self, info, **kwargs):
        id = kwargs.get('id')
        event = kwargs.get('event')

        if id:
            return EventDay.objects.filter(id=id)
        if event:
            return EventDay.objects.filter(event_id=event)
        return EventDay.objects.all()