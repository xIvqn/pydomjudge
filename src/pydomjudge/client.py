from typing import List

import requests
from requests.auth import HTTPDigestAuth

from pydomjudge.models.main import Contest, Clarification
from pydomjudge.models.request import ClarificationPost


class DOMJudge:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = HTTPDigestAuth(username, password)


    def get_contests(self) -> List[Contest]:
        response = self.session.get(f"{self.base_url}/api/v4/contests")
        response.raise_for_status()
        return [Contest(**item) for item in response.json()]

    def submit_clarification(self, cid: Union[str, int], data: ClarificationPost) -> Clarification:
        response = self.session.post(
            f"{self.base_url}/api/v4/contests/{cid}/clarifications",
            json=data.dict()
        )
        response.raise_for_status()
        return Clarification(**response.json())
