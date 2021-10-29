from .common import *


class Config:
    broker_url = env("CELERY_BROKER_URL", default="redis://redis:6379")
