import graphene

from graphene_django.types import DjangoObjectType

from .models import Venue


class VenueSchemaType(DjangoObjectType):
    class Meta:
        model = Venue


class LocationsQuery(object):
    pass
