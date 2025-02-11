from typing import List, Union

import requests
from requests.auth import HTTPDigestAuth

from pydomjudge.models.main import Contest, Clarification, Submission, User, Award, Balloon
from pydomjudge.models.request import ClarificationPost
from pydomjudge.models.response import Scoreboard, AccessInformation
from pydomjudge.models.shared import ArchiveFile, SourceCode


class DOMJudge:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = HTTPDigestAuth(username, password)

    # Access section
    def get_access_information(self, contest_id: Union[str, int], strict: bool = False) -> AccessInformation:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/access"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Accounts section
    def get_all_accounts(self, contest_id: Union[str, int], idlist: List[str] = None, team_id: str = None,
                         strict: bool = False) -> List[User]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/accounts"
        params = {
            "ids[]": idlist,
            "team_id": team_id,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_account(self, contest_id: Union[str, int], account_id: str, strict: bool = False) -> User:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/accounts/{account_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_current_account(self, contest_id: Union[str, int], strict: bool = False) -> User:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/account"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Awards section
    def get_all_awards(self, contest_id: Union[str, int], strict: bool = False) -> List[Award]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/awards"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_award(self, contest_id: Union[str, int], award_id: str, strict: bool = False) -> Award:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/awards/{award_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Balloons section
    def get_all_balloons(self, contest_id: Union[str, int], todo: bool = None) -> List[Balloon]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/balloons"
        params = {
            "todo": todo
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def mark_balloon_done(self, contest_id: Union[str, int], balloon_id: int) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/balloons/{balloon_id}/done"
        response = self.session.post(url)
        response.raise_for_status()

    # Clarifications section
    def get_all_clarifications(self, contest_id: Union[str, int], idlist: List[Union[str, int]] = None, problem: Union[str, int] = None, strict: bool = False) -> List[Clarification]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/clarifications"
        params = {
            "ids[]": idlist,
            "problem": problem,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_clarification(self, contest_id: Union[str, int], clarification_id: Union[str, int], strict: bool = False) -> Clarification:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/clarifications/{clarification_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def add_clarification(self, contest_id: Union[str, int], clarification: ClarificationPost) -> Clarification:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/clarifications"
        response = self.session.post(url, json=clarification)
        response.raise_for_status()
        return response.json()





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

    def get_scoreboard(self, contest_id: Union[str, int], allteams: bool = None, category: Union[str, int] = None,
                       country: str = None, affiliation: Union[str, int] = None, public: bool = None,
                       sortorder: int = None) -> Scoreboard:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/scoreboard"
        params = {
            "allteams": allteams,
            "category": category,
            "country": country,
            "affiliation": affiliation,
            "public": public,
            "sortorder": sortorder
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_submissions(self, contest_id: Union[str, int], idlist: List[Union[str, int]] = None, language_id: str = None,
                        strict: bool = False) -> List[Submission]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/submissions"
        params = {
            "ids[]": idlist,
            "language_id": language_id,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_submission(self, contest_id: Union[str, int], submission_id: Union[str, int], strict: bool = False) -> Submission:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/submissions/{submission_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_submission_files(self, contest_id: Union[str, int], submission_id: Union[str, int], strict: bool = False) -> List[ArchiveFile]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/submissions/{submission_id}/files"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.content

    def get_submission_source_code(self, contest_id: Union[str, int], submission_id: Union[str, int], strict: bool = False) -> List[SourceCode]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/submissions/{submission_id}/source-code"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
