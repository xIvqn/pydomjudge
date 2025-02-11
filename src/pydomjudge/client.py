from typing import List

import requests
from requests.auth import HTTPBasicAuth

from pydomjudge.models.main import Contest, Clarification
from pydomjudge.models.request import ClarificationPost


class DOMJudge:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)

    def get_contests(self) -> List[Contest]:
        response = requests.get(f"{self.base_url}/api/v4/contests", auth=self.auth)
        data = response.json()

        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f"{response.status_code} Client Error: {data.get('error', '')}")

        return [Contest(**item) for item in response.json()]

    def submit_clarification(self, cid: str, data: ClarificationPost) -> Clarification:
        response = requests.post(
            f"{self.base_url}/api/v4/contests/{cid}/clarifications",
            json=data.dict(),
            auth=self.auth
        )
        return Clarification(**response.json())
