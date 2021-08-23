import abc


class SMSBackend(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def send_verification_code(phone, text):
        pass
