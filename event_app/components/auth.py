from datetime import timedelta

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'accounts.User'

GRAPHQL_AUTH = {
    'SMS_BACKEND': 'apps.authentication.sms_backends.kaveh_negar.KavehNegar',
}

GRAPHQL_JWT = {
    'JWT_ENCODE_HANDLER': 'apps.authentication.utils.jwt_encode',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_REUSE_REFRESH_TOKENS': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=5),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}

AUTHENTICATION_BACKENDS = [
    "apps.authentication.backends.GraphQLAuthBackend",
]
