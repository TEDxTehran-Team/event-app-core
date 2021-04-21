from apps.authentication.sms_backends import SMSBackend


class KavehNegar(SMSBackend):
    @staticmethod
    def send(phone, text):
        print(phone, text)  # TODO
