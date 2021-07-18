import graphene
from graphene_django.types import DjangoObjectType

from apps.accounts.models import User
from apps.authentication.settings import graphql_auth_settings as app_settings


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = app_settings.USER_NODE_FILTER_FIELDS
        exclude = app_settings.USER_NODE_EXCLUDE_FIELDS

    pk = graphene.Int()

    def resolve_pk(self, info):
        return self.pk

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.select_related("status")


class AccountsQuery(graphene.ObjectType):
    me = graphene.Field(UserNode)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_authenticated:
            return user
        return None
