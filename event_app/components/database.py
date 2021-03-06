from .common import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASE_URL = env('DATABASE_URL', default="postgres://postgres:postgres@db:5432/db")
DATABASES = {
    'default': {
        **env.db(default=DATABASE_URL),
        'ATOMIC_REQUESTS': True
    },
}

FIXTURE_DIRS = ("event_app/fixtures/",)
