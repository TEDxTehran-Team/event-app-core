import graphene

from apps.organizers.schema import OrganizersQuery


class Query(OrganizersQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
