from apps.sponsors.schema import SponsorsQuery
import graphene

from apps.organizers.schema import OrganizersQuery
from apps.events.schema import EventsQuery
from apps.gallery.schema import AlbumsQuery
from apps.locations.schema import LocationsQuery
from apps.talks.schema import TalksQuery
from apps.timelines.schema import TimelinesQuery
from apps.news.schema import NewsQuery


class Query(
        OrganizersQuery,
        EventsQuery,
        AlbumsQuery,
        LocationsQuery,
        TalksQuery,
        TimelinesQuery,
        NewsQuery,
        SponsorsQuery,
        graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
