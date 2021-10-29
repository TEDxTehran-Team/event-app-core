import graphene
from graphql_jwt.decorators import login_required

from apps.networking.constants import Messages
from apps.networking.models import MatchmakingRequest
from apps.networking.schema import MatchmakingRequestType
from event_app.graphql.bases import Output


class MatchmakingRequestMixin(Output):
    request = graphene.Field(MatchmakingRequestType)

    @classmethod
    @login_required
    def resolve_mutation(cls, root, info):
        existing_request = MatchmakingRequest.objects.filter(
            user=info.context.user,
            date_expired__isnull=True,
            date_matched__isnull=True,
        ).first()
        if existing_request:
            return cls(success=False, errors=Messages.DUPLICATE_MATCHMAKING, request=existing_request)

        request = MatchmakingRequest.objects.create(
            user=info.context.user,
        )
        return cls(success=True, request=request)
