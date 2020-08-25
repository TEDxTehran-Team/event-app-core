from apps.events.schema import EventSchemaType
from apps.organizers.models import Organizer
from apps.events.models import Event
import graphene
import random 

from graphene_django.types import DjangoObjectType, ObjectType

from .models import Talk, Speaker


class SpeakerSchema(DjangoObjectType):
    class Meta:
        model = Speaker

    image_url = graphene.String()

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None



class TalkSchemaType(DjangoObjectType):
    class Meta:
        model = Talk

    event_id = graphene.Int()
    def resolve_event_id(self, info):
        return graphene.Int(resolver=lambda  my_obj, resolve_obj: my_obj.section.session.day.event.id)

class TalksWithEventSchemaType(ObjectType):
    talks = graphene.List(TalkSchemaType)
    event = graphene.Field(EventSchemaType)

    def resolve_talks(self, info, **kwargs):
        return Talk.objects.filter(section__session__day__event_id=self.event.id)

    def resolve_event(self, info, **kwargs):
        return Event.objects.get(id=self.event.id)

class TalksQuery(object):
    talk = graphene.Field(TalkSchemaType, id=graphene.Int(required=True), organizer=graphene.Int())    
    talks = graphene.List(TalkSchemaType, id=graphene.Int(), organizer=graphene.Int())
    talks_with_event = graphene.List(TalksWithEventSchemaType, organizer=graphene.Int())

    speaker = graphene.Field(SpeakerSchema, id=graphene.Int(required=True), organizer=graphene.Int())
    speakers = graphene.List(SpeakerSchema, id=graphene.Int(), organizer=graphene.Int())
    
    featured_talk = graphene.Field(TalkSchemaType, organizer=graphene.Int())
    suggested_talk = graphene.List(TalkSchemaType, talk=graphene.Int(required=True))

    def resolve_talks_with_event(self, info, **kwargs):
        orgnizer_id = kwargs.get('organizer', None)
        if orgnizer_id is None:
            orgnizer_id = Organizer.objects.first().id
        result = []
        events = Event.objects.filter(organizer_id=orgnizer_id)

        for item in events:
            a = TalksWithEventSchemaType()
            a.event = item
            result.append(a)
        
        return result

    def resolve_speaker(self, info, **kwargs):
        organizer_id = kwargs.get('organizer', None)
        if organizer_id is None:
            organizer_id = Organizer.objects.first().id
        
        return Speaker.objects.get(id=kwargs.get('id'), organizer_id=organizer_id)

    def resolve_talk(self, info, **kwargs):
        organizer_id = kwargs.get('organizer', None)
        if organizer_id is None:
            organizer_id = Organizer.objects.first().id

        return Talk.objects.get(id=kwargs.get('id'),section__session__day__event__organizer_id=organizer_id)

    def resolve_talks(self, info, **kwargs):
        organizer_id = kwargs.get('organizer', None)
        if organizer_id is None:
            organizer_id = Organizer.objects.first().id
        id = kwargs.get('id')
        if id:
            return Talk.objects.filter(id=kwargs.get('id'),section__session__day__event__organizer_id=organizer_id)
        else:
            return Talk.objects.filter(section__session__day__event__organizer_id=organizer_id)


    def resolve_speakers(self, info, **kwargs):
        organizer_id = kwargs.get('organizer', None)
        if organizer_id is None:
            organizer_id = Organizer.objects.first().id
        id = kwargs.get('id')
        if id:
            return Speaker.objects.filter(organizer_id=organizer_id, id=id)
        else:
            return Speaker.objects.filter(organizer_id=organizer_id)

    def resolve_featured_talk(self, info, **kwargs):
        organizer_id = kwargs.get('organizer')
        if organizer_id is None:
            organizer_id = Organizer.objects.first().id
        items = Talk.objects.filter(section__session__day__event__organizer_id=organizer_id)
        return random.choice(items)

    def resolve_suggested_talk(self, info, **kwargs):
        talk_id = kwargs.get('talk')
        organizer_id = Talk.objects.get(id=talk_id).section.session.day.event.organizer.id
        items = Talk.objects.filter(section__session__day__event__organizer_id=organizer_id)
        return [random.choice(items)]

