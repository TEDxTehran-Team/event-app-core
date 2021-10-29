from urllib.parse import urljoin

import backoff
import requests
from django.conf import settings


@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_time=5)
def new_chat(session: requests.Session, user_id, recipient_id):
    response = session.post(urljoin(settings.CHAT_HOST, '/new'), data={
        'user_id': user_id,
        'recipient_id': recipient_id,
    })
    data = response.json()
    if not data.get('status'):
        raise requests.exceptions.RequestException()
    return data['data']['conversation_id']
