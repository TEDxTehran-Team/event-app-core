import graphene

from apps.organizers.schema import OrganizersQuery
from apps.events.schema import EventsQuery
from apps.gallery.schema import AlbumsQuery
from apps.locations.schema import LocationsQuery
from apps.talks.schema import TalksQuery


class Query(
        OrganizersQuery,
        EventsQuery,
        AlbumsQuery,
        LocationsQuery,
        TalksQuery,
        graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
