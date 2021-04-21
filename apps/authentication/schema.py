from django.contrib.auth import get_user_model

import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from . import mutations
from .settings import graphql_auth_settings as app_settings


class UserNode(DjangoObjectType):
    class Meta:
        model = get_user_model()
        filter_fields = app_settings.USER_NODE_FILTER_FIELDS
        exclude = app_settings.USER_NODE_EXCLUDE_FIELDS
        interfaces = (graphene.relay.Node,)
        skip_registry = True

    pk = graphene.Int()

    def resolve_pk(self, info):
        return self.pk

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.select_related("status")


class UserQuery(graphene.ObjectType):
    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)


class MeQuery(graphene.ObjectType):
    me = graphene.Field(UserNode)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_authenticated:
            return user
        return None
