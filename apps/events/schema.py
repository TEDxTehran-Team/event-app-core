import graphene

from graphene_django.types import DjangoObjectType

from .models import Event, EventLink, EventType, AboutEvent


class EventSchemaType(DjangoObjectType):
    class Meta:
        model = Event
    
    banner_url = graphene.String(description="Image url of the banner field")
    logo_url = graphene.String(description="Image url of the logo field")

    def resolve_banner_url(self, info):
        if self.banner:
            return self.banner.url
        return None
    
    def resolve_logo_url(self, info):
        if self.logo:
            return self.logo.url
        return None


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
    event_description = """
    Retrieves Event data of the given id.
    """
    event = graphene.Field(EventSchemaType, id=graphene.Int(required=True), description=event_description)
    all_event = graphene.List(EventSchemaType)
    event_by_organizer = graphene.List(EventSchemaType, organization=graphene.Int(required=True))

    def resolve_all_event(self, info, **kwargs):
        return Event.objects.all()

    def resolve_event(self, info, **kwargs):
        return Event.objects.get(id=kwargs.get('id'))

    def resolve_event_by_organizer(self, info, **kwargs):
        id = kwargs.get('organizer')
        return Event.objects.filter(organizer__id=id)
