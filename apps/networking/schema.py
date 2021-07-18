import graphene
from graphene_django import DjangoObjectType

from apps.networking.models import Interest


class InterestType(DjangoObjectType):
    class Meta:
        model = Interest
        fields = ("id", "name")


class NetworkingQuery(graphene.ObjectType):
    interests = graphene.List(InterestType)

    def resolve_interests(root, info, **kwargs):  # noqa
        return Interest.objects.all()
