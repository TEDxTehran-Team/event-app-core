from django.utils.translation import gettext as _


class Messages:
    INVALID_TOKEN = [{"message": _("Invalid token."), "code": "invalid_token"}]
    EXPIRED_TOKEN = [{"message": _("Expired token."), "code": "expired_token"}]
    INVALID_CREDENTIALS = [
        {
            "message": _("Please, enter valid credentials."),
            "code": "invalid_credentials",
        }
    ]
