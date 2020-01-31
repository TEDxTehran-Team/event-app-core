from django.utils.translation import ugettext as _


class SectionType:
    GENERIC = 'generic'
    TALK = 'talk'
    PERFORMANCE = 'performance'
    ACTIVITY = 'activity'
    ENTERTAINMENT = 'entertainment'

    choices = (
        (GENERIC, _("Generic")),
        (TALK, _("Talks")),
        (PERFORMANCE, _("Performance")),
        (ACTIVITY, _("Activity")),
        (ENTERTAINMENT, _("Entertainment")),
    )
