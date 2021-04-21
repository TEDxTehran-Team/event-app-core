import abc


class SMSBackend(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def send(phone, text):
        pass
