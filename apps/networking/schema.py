import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from apps.networking.models import Interest, MatchmakingRequest, Match


class InterestType(DjangoObjectType):
    class Meta:
        model = Interest
        fields = ("id", "name")


class MatchmakingRequestType(DjangoObjectType):
    class Meta:
        model = MatchmakingRequest


class MatchType(DjangoObjectType):
    class Meta:
        model = Match


class NetworkingQuery(graphene.ObjectType):
    interests = graphene.List(InterestType)
    matchmaking_request = graphene.Field(MatchmakingRequestType)

    def resolve_interests(root, info, **kwargs):  # noqa
        return Interest.objects.all()

    @login_required
    def resolve_matchmaking_request(root, info, **kwargs):  # noqa
        return MatchmakingRequest.objects.filter(user=info.context.user).order_by('-date_created').first()
