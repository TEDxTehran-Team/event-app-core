from apps.accounts.schema import AccountsQuery
from apps.authentication.mutations import AuthMutation
from apps.accounts.mutations import AccountsMutation
from apps.networking.mutations import NetworkingMutation
from apps.sponsors.schema import SponsorsQuery
import graphene

from apps.organizers.schema import OrganizersQuery
from apps.events.schema import EventsQuery
from apps.gallery.schema import AlbumsQuery
from apps.locations.schema import LocationsQuery
from apps.talks.schema import TalksQuery
from apps.timelines.schema import TimelinesQuery
from apps.notifications.schema import NotificationsQuery
from apps.news.schema import NewsQuery
from apps.networking.schema import NetworkingQuery


class Mutation(
        AuthMutation,
        AccountsMutation,
        NetworkingMutation,
        graphene.ObjectType
):
    pass


class Query(
        AccountsQuery,
        OrganizersQuery,
        EventsQuery,
        AlbumsQuery,
        LocationsQuery,
        TalksQuery,
        TimelinesQuery,
        NotificationsQuery,
        NewsQuery,
        SponsorsQuery,
        NetworkingQuery,
        graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
