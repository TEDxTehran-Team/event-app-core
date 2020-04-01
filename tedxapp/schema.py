import graphene

from apps.organizers.schema import OrganizersQuery
from apps.events.schema import EventsQuery


class Query(OrganizersQuery, EventsQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
