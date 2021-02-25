from .common import *

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = env("LANGUAGE_CODE", default="en")

LANGUAGES = [
    ("en", "English"),
]

TIME_ZONE = env("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / "locale",
]
