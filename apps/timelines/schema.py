import graphene

from graphene_django.types import DjangoObjectType

from .models import EventDay, Session, Section


class EventDaySchemaType(DjangoObjectType):
    class Meta:
        model = EventDay


class SessionSchemaType(DjangoObjectType):
    class Meta:
        model = Session

    image_url = graphene.String(description="Image url for the image field")

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None

class SectionSchemaType(DjangoObjectType):
    class Meta:
        model = Section

    image_url = graphene.String(description="Image url for the image field")
    cover_url = graphene.String(description="Image url for the cover field")

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None
    
    def resolve_cover_url(self, info):
        if self.cover:
            return self.cover.url
        return None


class TimelinesQuery(object):
    event_day_description = """
    Returns EventDay object if id is provided otherwise a list of EventDays. If event is provided, it will search among that Event's
    EventDays.
    """
    event_day = graphene.Field(
        EventDaySchemaType,
        id=graphene.Int(description="EventDay Id"),
        event=graphene.Int(description="Event Id"),
        description=event_day_description)
    session_description = """
    Returns Session with a given ID
    """
    session = graphene.Field(SessionSchemaType, id=graphene.Int(required=True, description="Session Id"), description=session_description)
    section_description = """
    Returns Section with a given ID
    """
    section = graphene.Field(SectionSchemaType, id=graphene.Int(required=True, description="Section Id"), description=section_description)

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