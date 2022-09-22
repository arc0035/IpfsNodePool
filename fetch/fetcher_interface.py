import abc
from fake_useragent import UserAgent

class FetcherInterface(abc.ABCMeta):
    user_agent = UserAgent()

    @abc.abstractmethod
    def fetch(self):
        return NotImplemented

    @abc.abstractmethod
    def url(self):
        return NotImplemented