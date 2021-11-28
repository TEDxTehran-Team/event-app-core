from calendar import timegm
from datetime import datetime

from graphql_jwt.settings import jwt_settings


def jwt_payload(user, context=None):
    username = user.get_username()

    if hasattr(username, "pk"):
        username = username.pk

    exp = datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA

    payload = {
        "sub": user.id,
        user.USERNAME_FIELD: username,
        "name": ((user.first_name or '') + ' ' + (user.last_name or '')).strip(),
        "exp": timegm(exp.utctimetuple()),
    }

    if jwt_settings.JWT_ALLOW_REFRESH:
        payload["origIat"] = timegm(datetime.utcnow().utctimetuple())

    if jwt_settings.JWT_AUDIENCE is not None:
        payload["aud"] = jwt_settings.JWT_AUDIENCE

    if jwt_settings.JWT_ISSUER is not None:
        payload["iss"] = jwt_settings.JWT_ISSUER

    return payload
