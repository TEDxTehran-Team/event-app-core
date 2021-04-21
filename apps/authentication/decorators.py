from functools import wraps

from .constants import Messages


def login_required(fn):
    @wraps(fn)
    def wrapper(cls, root, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            return cls(success=False, errors=Messages.UNAUTHENTICATED)
        return fn(cls, root, info, **kwargs)

    return wrapper
