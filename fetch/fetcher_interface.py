import abc
from helper.useragent_faker import ua
import requests
from requests.adapters import HTTPAdapter, Retry
class FetcherInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def parse(self, resp):
        return NotImplemented

    @abc.abstractmethod
    def url(self):
        return NotImplemented

    def fetch(self):
        url_str = self.url()
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        resp = session.get(url_str, headers={
            'User-Agent': ua.random
        })

        if resp.status_code == 200:
            self.parse(resp)
        else:
            print('http error %s' % resp.status_code)

