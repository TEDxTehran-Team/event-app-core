import graphene

from apps.organizers.schema import OrganizersQuery
from apps.events.schema import EventsQuery
from apps.gallery.schema import AlbumsQuery


class Query(OrganizersQuery, EventsQuery, AlbumsQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
