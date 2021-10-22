from calendar import timegm
from datetime import datetime

import graphene
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from graphene.types.generic import GenericScalar
from graphql_jwt.exceptions import JSONWebTokenError, JSONWebTokenExpired
from graphql_jwt.refresh_token.shortcuts import refresh_token_lazy
from graphql_jwt.settings import jwt_settings

from apps.accounts.models import User
from event_app.graphql.bases import Output
from .constants import Messages
from .forms import AuthenticateForm, VerifyAuthenticationForm
from .models import AuthenticationAttempt
from ..accounts.schema import UserNode


class AuthenticateMixin(Output):
    """
    Start authentication process for the specified phone number.

    Sends account verification sms.
    """

    token = graphene.String(description="Identifies this specific login attempt - pass this token on the verify_authentication mutation")

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        with transaction.atomic():
            try:
                user = User.objects.get(phone=kwargs.get('phone'))
            except User.DoesNotExist:
                user = None
            f = AuthenticateForm(kwargs, instance=user)
            if f.is_valid():
                user, attempt = f.save()

                attempt.send_verification_code()

                return cls(success=True, token=attempt.token)
            else:
                return cls(success=False, errors=f.errors.get_json_data())


class VerifyAuthenticationMixin(Output):
    """
    Verify the verification code passed by the user.

    If the code is valid, logs the user in and returns
    token and refresh token and the user's details.
    """

    payload = GenericScalar()
    token = graphene.String(description="OAuth authorization token")
    refresh_token = graphene.String(description="OAuth refresh token")
    refresh_expires_in = graphene.Int()
    user = graphene.Field(UserNode)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        with transaction.atomic():
            try:
                attempt = AuthenticationAttempt.objects.get(token=kwargs.get('token'))
                f = VerifyAuthenticationForm(kwargs, instance=attempt)
                if f.is_valid():
                    f.save()

                    payload = jwt_settings.JWT_PAYLOAD_HANDLER(attempt.user)
                    token = jwt_settings.JWT_ENCODE_HANDLER(payload)
                    refresh_token = refresh_token_lazy(attempt.user)
                    refresh_expires_in = (
                            timegm(datetime.utcnow().utctimetuple()) +
                            jwt_settings.JWT_REFRESH_EXPIRATION_DELTA.total_seconds()
                    )

                    return cls(success=True,
                               user=attempt.user,
                               token=token,
                               refresh_token=refresh_token,
                               refresh_expires_in=refresh_expires_in,
                               payload=payload)
                else:
                    return cls(success=False, errors=f.errors.get_json_data())
            except ObjectDoesNotExist:
                return cls(success=False, errors=Messages.INVALID_CREDENTIALS)


class VerifyOrRefreshOrRevokeTokenMixin(Output):
    """
    Same as `grapgql_jwt` implementation, with standard output.
    """

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            return cls.parent_resolve(root, info, **kwargs)
        except JSONWebTokenExpired:
            return cls(success=False, errors=Messages.EXPIRED_TOKEN, payload={})
        except JSONWebTokenError:
            return cls(success=False, errors=Messages.INVALID_TOKEN, payload={})
