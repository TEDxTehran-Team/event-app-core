# Application definition

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "graphene_django",
    "rest_framework",
    "corsheaders",
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",
]

PROJECT_APPS = [
    "apps.authentication",
    "apps.accounts",
    "apps.utils",
    "apps.applications",
    "apps.organizers",
    "apps.locations",
    "apps.events",
    "apps.timelines",
    "apps.activities",
    "apps.talks",
    "apps.gallery",
    "apps.notifications",
    "apps.attendees",
    "apps.news",
    "apps.sponsors",
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS
