import graphene

from graphene_django.types import DjangoObjectType

from .models import Venue


class VenueSchemaType(DjangoObjectType):
    class Meta:
        model = Venue

    map_image_url = graphene.String()

    def resolve_map_image_url(self, info):
        if self.map_image:
            return self.map_image.url
        return None

class LocationsQuery(object):
    pass
