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
    event_id = graphene.Int()

    def resolve_talks(self, info, **kwargs):
        return Talk.objects.filter(section__session__day__event_id=self.event_id)


class TalksQuery(object):
    all_talks = graphene.List(TalkSchemaType)
    talk = graphene.Field(TalkSchemaType, id=graphene.Int(required=True))
    talks_by_event = graphene.List(TalkSchemaType, event=graphene.Int(required=True))
    talks_by_organizer = graphene.List(TalkSchemaType, organizer=graphene.Int(required=True))
    talks_with_event_by_organizer = graphene.List(TalksWithEventSchemaType, organizer=graphene.Int(required=True))
    speaker = graphene.Field(SpeakerSchema, id=graphene.Int(required=True))
    speakers_by_organizer = graphene.List(SpeakerSchema, organizer=graphene.Int(required=True))
    featured_talk = graphene.Field(TalkSchemaType, organizer=graphene.Int(required=True))
    suggest_talk = graphene.Field(TalkSchemaType, talk=graphene.Int(required=True))

    def resolve_talks_with_event_by_organizer(self, info, **kwargs):
        id = kwargs.get('organizer')
        result = []
        events = Talk.objects.filter(section__session__day__event__organizer_id=id)
        print(len(events))
        for item in events:
            a = TalksWithEventSchemaType()
            a.event_id = item.id
            result.append(a)
        
        return result

    def resolve_speaker(self, info, **kwargs):
        return Speaker.objects.get(id=kwargs.get('id'))

    def resolve_all_talks(self, info, **kwargs):
        return Talk.objects.all()

    def resolve_talk(self, info, **kwargs):
        return Talk.objects.get(id=kwargs.get('id'))

    def resolve_talks_by_event(self, info, **kwargs):
        id = kwargs.get('event')
        return Talk.objects.filter(section__session__day__event_id=id)

    def resolve_speakers_by_organizer(self, info, **kwargs):
        id = kwargs.get('organizer')
        return Speaker.objects.filter(organizer_id=id)
    
    def resolve_talks_by_organizer(self, info, **kwargs):
        id = kwargs.get('organizer')
        return Talk.objects.filter(section__session__day__event__organizer_id=id)

    def resolve_featured_talk(self, info, **kwargs):
        id = kwargs.get('organizer')
        items = Talk.objects.filter(section__session__day__event__organizer_id=id)
        return random.choice(items)

    def resolve_featured_talk(self, info, **kwargs):
        items = Talk.objects.all()
        return random.choice(items)


    # def resolve_walks_with_event_by_organizer(self, info, **kwargs):

