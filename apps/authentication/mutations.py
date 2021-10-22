import graphene
import graphql_jwt

from event_app.graphql.bases import MutationMixin, DynamicArgsMixin
from .mixins import (
    AuthenticateMixin,
    VerifyAuthenticationMixin,
    VerifyOrRefreshOrRevokeTokenMixin,
)


class Authenticate(MutationMixin, DynamicArgsMixin, AuthenticateMixin, graphene.Mutation):

    __doc__ = AuthenticateMixin.__doc__

    _required_args = ["phone"]
    _args = ["phone"]


class VerifyAuthentication(
    MutationMixin, DynamicArgsMixin, VerifyAuthenticationMixin, graphene.Mutation
):
    __doc__ = VerifyAuthenticationMixin.__doc__
    _required_args = ["token", "verification_code"]


class VerifyToken(MutationMixin, VerifyOrRefreshOrRevokeTokenMixin, graphql_jwt.Verify):
    __doc__ = VerifyOrRefreshOrRevokeTokenMixin.__doc__


class RefreshToken(
    MutationMixin, VerifyOrRefreshOrRevokeTokenMixin, graphql_jwt.Refresh
):
    __doc__ = VerifyOrRefreshOrRevokeTokenMixin.__doc__


class RevokeToken(MutationMixin, VerifyOrRefreshOrRevokeTokenMixin, graphql_jwt.Revoke):
    __doc__ = VerifyOrRefreshOrRevokeTokenMixin.__doc__


class AuthMutation(graphene.ObjectType):
    authenticate = Authenticate.Field()
    verify_authentication = VerifyAuthentication.Field()

    # django-graphql-jwt inheritances
    verify_token = VerifyToken.Field()
    refresh_token = RefreshToken.Field()
    revoke_token = RevokeToken.Field()
