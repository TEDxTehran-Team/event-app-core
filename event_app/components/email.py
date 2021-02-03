from .common import *

EMAIL_CONFIG = env.email_url('EMAIL_URL', default='smtp://user:password@localhost:25')
vars().update(EMAIL_CONFIG)

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="updates@example.com")
