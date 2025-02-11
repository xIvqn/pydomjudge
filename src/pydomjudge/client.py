import requests
from requests.auth import HTTPBasicAuth


class DOMJudge:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)
