import urllib.parse
import pytest
import requests

class HostSession(requests.Session):
    def __init__(self, host):
        self.host = host
        super().__init__()

    def request(self, method, url, *args, **kwargs):
        url = urllib.parse.urljoin(self.host, url)
        return super().request(method, url, *args, **kwargs)

@pytest.fixture()
def http_client():
    host = 'https://b2b2c.dev.sberdevices.ru'

    s = HostSession(host)
    yield s
    s.close()
