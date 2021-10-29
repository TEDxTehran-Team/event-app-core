import graphene

from apps.networking.mixins import MatchmakingRequestMixin
from event_app.graphql.bases import MutationMixin, DynamicArgsMixin


class MatchmakingRequestMutation(
    MutationMixin, DynamicArgsMixin, MatchmakingRequestMixin, graphene.Mutation
):
    pass


class NetworkingMutation(graphene.ObjectType):
    matchmaking_request = MatchmakingRequestMutation.Field()
