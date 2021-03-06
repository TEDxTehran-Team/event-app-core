from django.utils import translation
from apps.gallery.models import Album, Photo, Video
from apps.talks.models import Speaker, Talk
from apps.timelines.models import EventDay, Section, Session
from datetime import datetime
from apps.organizers.models import Organizer
from apps.news.models import News
from apps.events.models import EventType, Event
from apps.locations.models import Venue
import json


from apps.sponsors.models import Sponsors, SponsorsType
def data_read(filename):
    data = {}
    with open(filename, "r") as file:
        data = json.loads(file.read())

    return data

def write_translation(translation):
    with open("translation.json", "w") as file:
        file.write(json.dumps(translation))

def read_translation():
    with open("translation.json", "r") as file:
        data = json.loads(file.read())
        return data

def save_translation_id(translation, key, original, new):
    if not translation.get(key):
        translation[key] = {}
    translation[key][original] = new


def import_sponsors(data, translation):
    general_type = SponsorsType.objects.get_or_create(title="حامی رویداد")

    for id, item in data["sponsors"].items():
        instance = Sponsors.objects.create(
            title=item["name"],
            description=item["description"],
            link=item["url"],
            logo=item["logo"],
            type_id=general_type[0].id
        )
        save_translation_id(translation, "sponsors", id, instance.id)

    write_translation(translation)


def import_events(data, translation):
    general_type = EventType.objects.get_or_create(title="Standard")
    default_organizer = Organizer.objects.first()
    for id, item in data["events"].items():
        venue = Venue.objects.create(
            title=item["location_name"] if item["location_name"] is not None else "no-name",
            address=item["location_address"],
            latitude=float(item["lat"]) if item["lat"] is not None else None,
            longitude=float(item["lng"]) if item["lng"] is not None else None,
            map_link=item["mapurl"],
            map_image=item["mapimg"],
            organizer=default_organizer
        )
        event = Event.objects.create(
            title=item["name"],
            description=item["description"],
            logo=item["logo"],
            banner=item["banner"],
            start_date=datetime.strptime(item["start_date"], '%Y-%m-%d %H:%M:%S%z'),
            end_date=datetime.strptime(item["end_date"], '%Y-%m-%d %H:%M:%S%z'),
            venue=venue,
            event_type=general_type[0],
            organizer=default_organizer
        )
        save_translation_id(translation, "events", id, event.id)
    write_translation(translation)

def import_days(data, translation):
    for id, item in data["days"].items():
        event = Event.objects.get(id=int(translation["events"][str(item["event_id"])]))
        day = EventDay.objects.create(
            event_id=event.id,
            date=datetime.strptime(item["date"], '%Y-%m-%d %H:%M:%S%z') if item["date"] is not None else event.start_date,
            title=item["title"] if item["title"] is not None else "no-title"
        )
        save_translation_id(translation, "days", id, day.id)
    write_translation(translation)

def import_sessions(data, translation):
    for id, item in data["sessions"].items():
        day = EventDay.objects.get(id=int(translation["days"][str(item["day_id"])]))
        session = Session.objects.create(
            day_id=day.id,
            start_time=datetime.strptime(item["start_time"], '%H:%M:%S') if item["start_time"] is not None else datetime.strptime("00:00:00", '%H:%M:%S'),
            end_time=datetime.strptime(item["end_time"], '%H:%M:%S') if item["end_time"] is not None else datetime.strptime("23:59:59", '%H:%M:%S'),
            title=item["title"] if item["title"] is not None else "no-title",
            description=item["description"] or "",
            image=item["image_url"]
        )
        save_translation_id(translation, "sessions", id, session.id)
    write_translation(translation)

def import_talks(data, translation):
    for id, item in data["talks"].items():
        session_id=item["session_id"]
        event = Event.objects.get(id=int(translation["events"][str(item["event_id"])]))
        if session_id is None or session_id == "None":
            day = EventDay.objects.filter(event_id=event.id).first()
            if day is None:
                day = EventDay.objects.create(
                    event_id=event.id,
                    date=event.start_date,
                    title="روز اول"
                )
            session = Session.objects.create(
                day_id=day.id,
                start_time=datetime.strptime("00:00:00", '%H:%M:%S'),
                end_time=datetime.strptime("23:59:59", '%H:%M:%S'),
                title="سشن اول",
                description="",
            )
        else:
            print(item["session_id"])
            print(id)
            print(item)
            session = Session.objects.get(id=int(translation["sessions"][str(item["session_id"])]))
        
        section = Section.objects.create(
            session_id=session.id,
            start_time=session.start_time,
            end_time=session.end_time,
            title="بخش اول"
        )
        
        talk = Talk.objects.create(
            section_id = section.id,
            title=item["title"] if item["title"] is not None else "no-title",
            description=item["description"] or "",
            video_link=item["video_url"] or "",
            extra_link=item["additional_video_url"]or ""
        )
        save_translation_id(translation, "talks", id, talk.id)
    write_translation(translation)

def import_speakers(data, translation):
    for id, item in data["speakers"].items():
        default_organizer = Organizer.objects.first()
        speaker = Speaker.objects.create(
            organizer=default_organizer,
            image=item["image_url"] or "",
            title=item["name"] or "",
            description=item["description"] or ""
        )
        for talk_id in item["talks"]:
            talk = Talk.objects.get(id=int(translation["talks"][str(talk_id)]))
            speaker.event_id = talk.section.session.day.event.id
            speaker.save()
            talk.speakers.add(speaker)
            talk.save()
        save_translation_id(translation, "speakers", id, speaker.id)
    write_translation(translation)


def import_event_sponsorship(data, translation):
    for id, item in data["event_sponsorship"].items():
        event = Event.objects.get(id=int(translation["events"][str(item["event_id"])]))
        sponsor = Sponsors.objects.get(id=int(translation["sponsors"][str(item["sponsor_id"])]))
        sponsor.event.add(event)
        sponsor.save()

def import_photo_video(data, translation):
    for event in Event.objects.all():
        Album.objects.create(
            title = "آلبوم رویداد " + event.title,
            event = event,
            organizer = event.organizer
        )
    for id, item in data["photos"].items():
        album = Album.objects.filter(event_id=int(translation["events"][str(item["event_id"])])).first()
        photo = Photo.objects.create(
            image=item["file"],
            album=album,
            thumbnail=item["thumb"],
            link=item["web"]
        )
        save_translation_id(translation, "photos", id, photo.id)
    write_translation(translation)

def import_news(data, translation):
    for id, item in data["news"].items():
        print(item["title"])
        news = News.objects.create(
            title=item["title"],
            description=item["description"] or "",
            image=item["image_url"] or None,
            extra_link=item["external_url"] or "",
            date=datetime.strptime(item["date"], '%Y-%m-%d %H:%M:%S%z'),
            organizer_id=1
        )
        
        save_translation_id(translation, "news", id, news.id)
    write_translation(translation)




def fix_talk_images(data, translation):
    for id, item in data["talks"].items():
        talk = Talk.objects.get(id=int(translation["talks"][id]))
        talk.section.image=item["image_url"] or None
        print(item["image_url"])
        talk.save()
        



translation = read_translation()

full_data = data_read("data.json")
import_news(full_data, translation)




