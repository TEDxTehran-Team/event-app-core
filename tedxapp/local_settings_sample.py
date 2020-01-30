import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "$$o6fa&)^@=5jwaypeaw4a--(6mu&+4mmlh9$s57gxq2f_5d56"

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

EMAIL_HOST = "smtp.mailtrap.io"
EMAIL_HOST_USER = "7a64e2493f0f03"
EMAIL_HOST_PASSWORD = "785ddb0f962ca8"
EMAIL_PORT = "2525"

SITE_NAME = "TEDx App"
ADMIN_SITE_HEADER = "TEDx App Admin"

DEFAULT_FROM_EMAIL = "updates@example.com"

LANGUAGES = [
    ("en", "English"),
]

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"
