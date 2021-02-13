from apps.events.schema import EventSchemaType
from event_app.utility import get_organizer
from apps.organizers.models import Organizer
from apps.events.models import Event
import graphene
import random 

from graphene_django.types import DjangoObjectType, ObjectType

from .models import Talk, Speaker


class SpeakerSchema(DjangoObjectType):
    class Meta:
        model = Speaker

    image_url = graphene.String(description="Image url of the Speaker's image field")

    def resolve_image_url(self, info):
        if self.image:
            return self.image.url
        return None



class TalkSchemaType(DjangoObjectType):
    class Meta:
        model = Talk

    event_id = graphene.Int(description="Event Id of the talk")
    def resolve_event_id(self, info):
        return graphene.Int(resolver=lambda  my_obj, resolve_obj: my_obj.section.session.day.event.id)

class TalksWithEventSchemaType(ObjectType):
    talks = graphene.List(TalkSchemaType, description="List of the talks of the same event")
    event = graphene.Field(EventSchemaType, description="The event that the talks correspond to")

    def resolve_talks(self, info, **kwargs):
        return Talk.objects.filter(section__session__day__event_id=self.event.id)

    def resolve_event(self, info, **kwargs):
        return Event.objects.get(id=self.event.id)

class TalksQuery(object):
    talk_description="""
    Retrieves Talk data of the given id. If organizer is provided, it will search among that organizer's
    talks. Otherwise it will search among the talks of the organizer connected to the application token
    sent by the client.
    """
    talk = graphene.Field(TalkSchemaType, id=graphene.Int(required=True), organizer=graphene.Int(), description=talk_description)
    talks_description="""
    Same as Talk Query, with the only change that if id is not provided, it returns all the talks of the given organizer
    """
    talks = graphene.List(TalkSchemaType, id=graphene.Int(), organizer=graphene.Int(), description=talks_description)
    talks_with_event_description="""
    Returns a list of events and their talks. To be more exact, each item of the list contains an Event object and a list of Talk objects,
    each Talk object has an extra field called eventId that stores the Id of this talk's event. Again, if organizer is provided,
    it searchs among the talks of that organizer. Otherwise it will search among the talks of the organizer connected to the application token
    sent by the client.
    """
    talks_with_event = graphene.List(TalksWithEventSchemaType, organizer=graphene.Int(), description=talks_with_event_description)
    speaker_description = """
    Retrieves Speaker data of the given id. If organizer is provided, it will search among that organizer's
    speakers. Otherwise it will search among the speakers of the organizer connected to the application token
    sent by the client.
    """
    speaker = graphene.Field(SpeakerSchema, id=graphene.Int(required=True), organizer=graphene.Int(), description=speaker_description)
    speakers_description = """
    Same as Speaker Query, with the only change that if id is not provided, it returns all the speakers of the given organizer
    """
    speakers = graphene.List(SpeakerSchema, id=graphene.Int(), organizer=graphene.Int(), description=speakers_description)
    featured_talk_description = """
    Returns the featured talk of the organizer. If organizer is provided, it will search among that organizer's
    talks. Otherwise it will search among the talks of the organizer connected to the application token
    sent by the client.
    """
    featured_talk = graphene.Field(TalkSchemaType, organizer=graphene.Int(), description=featured_talk_description)
    suggested_talk_description = """
    Returns the suggested talk of the organizer. If organizer is provided, it will search among that organizer's
    talks. Otherwise it will search among the talks of the organizer connected to the application token
    sent by the client.
    """
    suggested_talks = graphene.List(TalkSchemaType, talk=graphene.Int(required=True), description=suggested_talk_description)

    def resolve_talks_with_event(self, info, **kwargs):
        organizer_id = get_organizer(info)
        result = []
        events = Event.objects.filter(organizer_id=organizer_id).order_by('-start_date')

        for item in events:
            a = TalksWithEventSchemaType()
            a.event = item
            result.append(a)
        
        return result

    def resolve_speaker(self, info, **kwargs):
        organizer_id = get_organizer(info)
        
        return Speaker.objects.get(id=kwargs.get('id'), organizer_id=organizer_id)

    def resolve_talk(self, info, **kwargs):
        organizer_id = get_organizer(info)

        return Talk.objects.get(id=kwargs.get('id'),section__session__day__event__organizer_id=organizer_id)

    def resolve_talks(self, info, **kwargs):
        organizer_id = get_organizer(info)
        id = kwargs.get('id')
        if id:
            return Talk.objects.filter(id=kwargs.get('id'),section__session__day__event__organizer_id=organizer_id)
        else:
            return Talk.objects.filter(section__session__day__event__organizer_id=organizer_id)


    def resolve_speakers(self, info, **kwargs):
        organizer_id = get_organizer(info)
        id = kwargs.get('id')
        if id:
            return Speaker.objects.filter(organizer_id=organizer_id, id=id)
        else:
            return Speaker.objects.filter(organizer_id=organizer_id)

    def resolve_featured_talk(self, info, **kwargs):
        organizer_id = get_organizer(info)
        items = Talk.objects.filter(section__session__day__event__organizer_id=organizer_id)
        return random.choice(items)

    def resolve_suggested_talks(self, info, **kwargs):
        talk_id = kwargs.get('talk')
        organizer_id = Talk.objects.get(id=talk_id).section.session.day.event.organizer.id
        items = Talk.objects.filter(section__session__day__event__organizer_id=organizer_id)
        return [random.choice(items)]

