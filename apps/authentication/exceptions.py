from django.utils.translation import gettext as _


class UserAlreadyVerified(Exception):
    def __init__(self):
        super().__init__(_("User already verified."))

