import http.client
from urllib import parse

from django.conf import settings

from apps.authentication.sms_backends import SMSBackend


class KaveNegar(SMSBackend):

    @staticmethod
    def send_verification_code(phone, code):
        params = parse.urlencode(
            {
                'template': 'tedxtehranlogin',
                'token': code,
                'receptor': phone,
            }
        )
        headers = {
            "Content-type": "application/x-www-form-urlencoded"
        }

        conn = http.client.HTTPSConnection("api.kavenegar.com")
        conn.request(
            "POST",
            f"/v1/{settings.KAVENEGAR_API_KEY}/verify/lookup.json",
            params,
            headers
        )

        response = conn.getresponse()
        data = response.read()

        return data
