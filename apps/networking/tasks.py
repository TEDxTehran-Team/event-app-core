import itertools
import logging
import operator
import typing

from celery import shared_task
from django.conf import settings
from django.utils.timezone import now
from requests import Session, RequestException

from apps.networking import chat
from apps.networking.models import MatchmakingRequest, Match
from event_app.celery import app


@app.task
def process_matchmaking():
    MatchmakingRequest.objects.filter(
        match__isnull=True,
        date_created__lt=now() - settings.MATCHMAKING_REQUEST_EXPIRY_PERIOD
    ).update(date_expired=now())

    requests = MatchmakingRequest.objects\
        .filter(date_matched__isnull=True, date_expired__isnull=True)\
        .select_related('user')\
        .all()

    pairs: typing.List[typing.Tuple[MatchmakingRequest, MatchmakingRequest]] = list(itertools.combinations(requests, 2))
    scores = {}
    for pair in pairs:
        common_interest_count = pair[0].user.interests.all().intersection(pair[1].user.interests.all()).count()
        scores[pair] = common_interest_count

    session = Session()

    found_user_ids = []
    for pair, score in sorted(scores.items(), key=operator.itemgetter(1), reverse=True):
        if pair[0].user.id in found_user_ids or pair[1].user.id in found_user_ids:
            continue
        found_user_ids.extend([pair[0].user.id, pair[1].user.id])
        try:
            conversation_id = chat.new_chat(session, pair[0].user.id, pair[1].user.id)
        except RequestException:
            logging.exception("Failed to create a new conversation")
            continue

        match = Match.objects.create(conversation_id=conversation_id)
        match.parties.add(pair[0].user, pair[1].user)


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(settings.CHAT_MATCHMAKING_INTERVAL.total_seconds(), process_matchmaking.s())
