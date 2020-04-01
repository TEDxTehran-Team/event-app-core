import graphene

from graphene_django.types import DjangoObjectType

from .models import Organizer, AboutOrganizer


class OrganizerType(DjangoObjectType):
    class Meta:
        model = Organizer


class AboutOrganizerType(DjangoObjectType):
    class Meta:
        model = AboutOrganizer


class OrganizersQuery(object):
    organizer = graphene.Field(OrganizerType)

    def resolve_organizer(self, info, **kwargs):
        # todo return organizer based on the application
        return Organizer.objects.first()