from event_app.utility import get_organizer
from apps.events.schema import EventSchemaType
from apps.organizers.models import Organizer
from apps.events.models import Event
import graphene

from graphene_django.types import DjangoObjectType, ObjectType

from .models import Sponsors, SponsorsType


class SponsorTypeSchemaType(DjangoObjectType):
    class Meta:
        model = SponsorsType


class SponsorSchemaType(DjangoObjectType):
    class Meta:
        model = Sponsors

    image_url = graphene.String()
    logo_url = graphene.String()

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None
    
    def resolve_logo_url(self, info):
        if self.logo:
            return self.logo.url
        return None

class SponsorsWithTypeSchemaType(ObjectType):
    sponsors = graphene.List(SponsorSchemaType, description="Event sponsors list")
    type = graphene.Field(SponsorTypeSchemaType, description="Sponsor Type")


class SponsorsQuery(object):
    sponsors_description = """
    Returns the sponsors list of a given event or organizer or returns a single sponser if the Id is provided.
    It first checks whether the sponser Id is provided. If not then it checks for the event Id. Finaly it checks
    for the organizer Id and if that was not provided, this query returns the sponsors list of the organizer that
    is connected to the application token provided by the client.
    """
    sponsors = graphene.List(
        SponsorSchemaType,
        id=graphene.Int(required=False, description="Sponsor's Id"),
        organizer=graphene.Int(required=False, description="Organizer's Id"),
        event=graphene.Int(required=False, description="Event's Id"),
        description=sponsors_description
    )

    sponsors_with_type_description = """
    Returns a list of sponsors and their corresponding types.
    To be more exact, each item of the list contains an SponsorType object and a list of Sponsor objects
    """

    sponsors_with_type = graphene.List(
        SponsorsWithTypeSchemaType,
        event=graphene.Int(required=True, description="Event's Id"),
        description=sponsors_with_type_description
    )

    def resolve_sponsors(self, info, **kwargs):
        event_id = kwargs.get('event', None)
        organizer_id = get_organizer(info)
        id = kwargs.get('id', None)

        if id:
            return Sponsors.objects.get(pk=id)
        if event_id:
            return Sponsors.objects.filter(event__id=event_id)
        
        
        return Sponsors.objects.filter(organizer__id=organizer_id)
    
    def resolve_sponsors_with_type(self, info, **kwargs):
        event_id = kwargs.get('event', None)
        types = SponsorsType.objects.all().order_by('-ordering')
        list = []
        for item in types:
            sponsors = Sponsors.objects.filter(event__id=event_id, type=item)
            if sponsors:
                result = SponsorsWithTypeSchemaType()
                result.sponsors = sponsors
                result.type = item
                list.append(result)

        return list
