import requests
from utils.logger import log

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def set_token(self, token):
        self.token = token
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def post(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        log.info(f"POST {url}")
        return self.session.post(url, **kwargs)

    def get(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        log.info(f"GET {url}")
        return self.session.get(url, **kwargs)

    def delete(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        log.info(f"DELETE {url}")
        return self.session.delete(url, **kwargs)

    def put(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        log.info(f"PUT {url}")
        return self.session.put(url, **kwargs)