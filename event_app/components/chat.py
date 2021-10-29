from datetime import timedelta

from .common import *


CHAT_HOST = env('CHAT_HOST', default='http://chat:3030/api/v1.0')
CHAT_MATCHMAKING_INTERVAL = timedelta(seconds=10)
