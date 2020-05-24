import graphene

from graphene_django.types import DjangoObjectType

from .models import Organizer, AboutOrganizer


class OrganizerSchemaType(DjangoObjectType):
    class Meta:
        model = Organizer

    logo_url = graphene.String(resolver=lambda my_obj, resolve_obj: my_obj.logo.url)


class AboutOrganizerSchemaType(DjangoObjectType):
    class Meta:
        model = AboutOrganizer


class OrganizersQuery(object):
    organizer = graphene.Field(OrganizerSchemaType,
                               id=graphene.Int())

    about_organizer = graphene.Field(AboutOrganizerSchemaType)

    def resolve_about_organizer(self, info, **kwargs):
        return AboutOrganizer.objects.first()

    def resolve_organizer(self, info, **kwargs):
        # todo return organizer based on the application
        id = kwargs.get("id")
        if id is not None:
            try:
                return Organizer.objects.get(id=id)
            except Organizer.DoesNotExist:
                return None

        return Organizer.objects.first()
