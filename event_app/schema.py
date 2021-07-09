from apps.accounts.schema import UserQuery, MeQuery
from apps.authentication.mutations import AuthMutation
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


class Mutation(
        AuthMutation,
        graphene.ObjectType
):
    pass


class Query(
        UserQuery,
        MeQuery,
        OrganizersQuery,
        EventsQuery,
        AlbumsQuery,
        LocationsQuery,
        TalksQuery,
        TimelinesQuery,
        NotificationsQuery,
        NewsQuery,
        SponsorsQuery,
        graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
