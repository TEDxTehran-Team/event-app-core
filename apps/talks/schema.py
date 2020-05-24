import graphene

from graphene_django.types import DjangoObjectType

from .models import Talk, Speaker


class SpeakerSchema(DjangoObjectType):
    class Meta:
        model = Speaker


class TalkSchemaType(DjangoObjectType):
    class Meta:
        model = Talk


class TalksQuery(object):
    all_talk = graphene.List(TalkSchemaType)
    talk = graphene.Field(TalkSchemaType, id=graphene.Int(required=True))
    talk_by_event = graphene.List(TalkSchemaType, event=graphene.Int(required=True))
    speaker = graphene.Field(SpeakerSchema, id=graphene.Int(required=True))

    def resolve_speaker(self, info, **kwargs):
        return Speaker.objects.get(id=kwargs.get('id'))

    def resolve_all_talk(self, info, **kwargs):
        return Talk.objects.all()

    def resolve_talk(self, info, **kwargs):
        return Talk.objects.get(id=kwargs.get('id'))

    def resolve_talk_by_event(self, info, **kwargs):
        id = kwargs.get('event')
        return Talk.objects.filter(section__session__day__event_id=id)
