from typing import List, Union, Dict

import requests
from requests.auth import HTTPDigestAuth

from pydomjudge.models.main import Contest, Clarification, Submission, User, Award, Balloon, ContestState, \
    ContestStatus, Event, ContestProblem, JudgementType, Language, TeamAffiliation, Judging, Judgehost, TeamCategory, \
    JudgingRun, Team
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

    # Contests section
    def get_all_contests(self, idlist: List[str] = None, only_active: bool = False, strict: bool = False) -> List[Contest]:
        url = f"{self.base_url}/api/v4/contests"
        params = {
            "ids[]": idlist,
            "onlyActive": only_active,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_contest(self, contest_id: Union[str, int], strict: bool = False) -> Contest:
        url = f"{self.base_url}/api/v4/contests/{contest_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def add_contest(self, contest_data: dict, strict: bool = False) -> str:
        url = f"{self.base_url}/api/v4/contests"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, files=contest_data)
        response.raise_for_status()
        return response.json()

    def change_contest_start_time(self, contest_id: Union[str, int], start_time: str, force: bool = False, strict: bool = False) -> str:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/starttime"
        params = {
            "strict": strict
        }
        data = {
            "start_time": start_time,
            "force": force
        }
        response = self.session.patch(url, params=params, data=data)
        response.raise_for_status()
        return response.json()

    def get_contest_banner(self, contest_id: Union[str, int], strict: bool = False) -> bytes:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/banner"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.content

    def set_contest_banner(self, contest_id: Union[str, int], banner: bytes, strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/banner"
        params = {
            "strict": strict
        }
        files = {
            "banner": banner
        }
        response = self.session.put(url, params=params, files=files)
        response.raise_for_status()

    def delete_contest_banner(self, contest_id: Union[str, int], strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/banner"
        params = {
            "strict": strict
        }
        response = self.session.delete(url, params=params)
        response.raise_for_status()

    def get_contest_yaml(self, contest_id: Union[str, int], strict: bool = False) -> str:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/contest-yaml"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.text

    def get_contest_state(self, contest_id: Union[str, int], strict: bool = False) -> ContestState:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/state"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_event_feed(self, contest_id: Union[str, int], since_id: str = None, types: List[str] = None,
                       stream: bool = True, strict: bool = False) -> List[Event]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/event-feed"
        params = {
            "since_id": since_id,
            "types": types,
            "stream": stream,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_contest_status(self, contest_id: Union[str, int], strict: bool = False) -> ContestStatus:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/status"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_samples_zip(self, contest_id: Union[str, int], strict: bool = False) -> bytes:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/samples.zip"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.content

    # Executables section
    def get_executable(self, executable_id: str, strict: bool = False) -> Dict:
        url = f"{self.base_url}/api/v4/executables/{executable_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # General section
    def get_api_version(self, strict: bool = False) -> Dict:
        url = f"{self.base_url}/api/v4/version"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_api_info(self, strict: bool = False) -> Dict:
        url = f"{self.base_url}/api/v4/info"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_api_root(self, strict: bool = False) -> Dict:
        url = f"{self.base_url}/api/v4/"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_general_status(self, strict: bool = False) -> List[Dict]:
        url = f"{self.base_url}/api/v4/status"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_user_info(self, strict: bool = False) -> User:
        url = f"{self.base_url}/api/v4/user"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_config(self, name: str = None, strict: bool = False) -> Dict:
        url = f"{self.base_url}/api/v4/config"
        params = {
            "name": name,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def update_config(self, config_data: Dict, strict: bool = False) -> Dict:
        url = f"{self.base_url}/api/v4/config"
        params = {
            "strict": strict
        }
        response = self.session.put(url, params=params, json=config_data)
        response.raise_for_status()
        return response.json()

    def check_config(self, strict: bool = False) -> Dict:
        url = f"{self.base_url}/api/v4/config/check"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_country_flag(self, country_code: str, size: str, strict: bool = False) -> bytes:
        url = f"{self.base_url}/api/v4/country-flags/{country_code}/{size}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.content

    # Problems section
    def get_all_problems(self, contest_id: Union[str, int], idlist: List[str] = None, strict: bool = False) -> List[ContestProblem]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/problems"
        params = {
            "ids[]": idlist,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_problem(self, contest_id: Union[str, int], problem_id: str, strict: bool = False) -> ContestProblem:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/problems/{problem_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def add_problem(self, contest_id: Union[str, int], problem_data: dict, strict: bool = False) -> str:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/problems"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, files=problem_data)
        response.raise_for_status()
        return response.json()

    def link_problem(self, contest_id: Union[str, int], problem_id: str, problem_data: dict, strict: bool = False) -> ContestProblem:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/problems/{problem_id}"
        params = {
            "strict": strict
        }
        response = self.session.put(url, params=params, json=problem_data)
        response.raise_for_status()
        return response.json()

    def unlink_problem(self, contest_id: Union[str, int], problem_id: str, strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/problems/{problem_id}"
        params = {
            "strict": strict
        }
        response = self.session.delete(url, params=params)
        response.raise_for_status()

    def get_problem_statement(self, contest_id: Union[str, int], problem_id: str, strict: bool = False) -> bytes:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/problems/{problem_id}/statement"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.content

    def add_problems(self, contest_id: Union[str, int], problems_data: dict, strict: bool = False) -> List[str]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/problems/add-data"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, files=problems_data)
        response.raise_for_status()
        return response.json()

    # Groups section
    def get_all_groups(self, contest_id: Union[str, int], idlist: List[str] = None, public: bool = None,
                       strict: bool = False) -> List[TeamCategory]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/groups"
        params = {
            "ids[]": idlist,
            "public": public,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def add_group(self, contest_id: Union[str, int], group_data: dict, strict: bool = False) -> TeamCategory:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/groups"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, json=group_data)
        response.raise_for_status()
        return response.json()

    def get_group(self, contest_id: Union[str, int], group_id: str, strict: bool = False) -> TeamCategory:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/groups/{group_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Judgehosts section
    def get_judgehosts(self, hostname: str = None, strict: bool = False) -> List[Judgehost]:
        url = f"{self.base_url}/api/v4/judgehosts"
        params = {
            "hostname": hostname,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def add_judgehost(self, strict: bool = False) -> List[Judging]:
        url = f"{self.base_url}/api/v4/judgehosts"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params)
        response.raise_for_status()
        return response.json()

    def update_judgehost(self, hostname: str, judgehost_data: dict, strict: bool = False) -> List[Judgehost]:
        url = f"{self.base_url}/api/v4/judgehosts/{hostname}"
        params = {
            "strict": strict
        }
        response = self.session.put(url, params=params, json=judgehost_data)
        response.raise_for_status()
        return response.json()

    def update_judging(self, hostname: str, judgetask_id: int, judging_data: dict, strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/judgehosts/update-judging/{hostname}/{judgetask_id}"
        params = {
            "strict": strict
        }
        response = self.session.put(url, params=params, json=judging_data)
        response.raise_for_status()

    def add_debug_info(self, hostname: str, judgetask_id: int, debug_info: dict, strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/judgehosts/add-debug-info/{hostname}/{judgetask_id}"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, json=debug_info)
        response.raise_for_status()

    def add_judging_run(self, hostname: str, judgetask_id: int, judging_run_data: dict,
                        strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/judgehosts/add-judging-run/{hostname}/{judgetask_id}"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, json=judging_run_data)
        response.raise_for_status()

    def report_internal_error(self, error_data: dict, strict: bool = False) -> int:
        url = f"{self.base_url}/api/v4/judgehosts/internal-error"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, json=error_data)
        response.raise_for_status()
        return response.json()

    def get_files(self, file_type: str, file_id: str, strict: bool = False) -> bytes:
        url = f"{self.base_url}/api/v4/judgehosts/get_files/{file_type}/{file_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.content

    def fetch_work_tasks(self, strict: bool = False) -> List[Dict]:
        url = f"{self.base_url}/api/v4/judgehosts/fetch-work"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params)
        response.raise_for_status()
        return response.json()

    # Judgements section
    def get_all_judgements(self, contest_id: Union[str, int], idlist: List[str] = None, result: str = None,
                           submission_id: str = None, strict: bool = False) -> List[Judging]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/judgements"
        params = {
            "ids[]": idlist,
            "result": result,
            "submission_id": submission_id,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_judgement(self, contest_id: Union[str, int], judgement_id: str, strict: bool = False) -> Judging:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/judgements/{judgement_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Judgement types section
    def get_all_judgement_types(self, contest_id: Union[str, int], idlist: List[str] = None,
                                strict: bool = False) -> List[JudgementType]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/judgement-types"
        params = {
            "ids[]": idlist,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_judgement_type(self, contest_id: Union[str, int], judgement_type_id: str,
                           strict: bool = False) -> JudgementType:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/judgement-types/{judgement_type_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Languages section
    def get_all_languages(self, contest_id: Union[str, int], idlist: List[str] = None, strict: bool = False) -> \
    List[Language]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/languages"
        params = {
            "ids[]": idlist,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_language(self, contest_id: Union[str, int], language_id: str, strict: bool = False) -> Language:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/languages/{language_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Metrics section
    def get_metrics(self, strict: bool = False) -> str:
        url = f"{self.base_url}/api/v4/metrics/prometheus"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.text

    # Organizations section
    def get_all_organizations(self, contest_id: Union[str, int], idlist: List[str] = None, country: str = None,
                              strict: bool = False) -> List[TeamAffiliation]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/organizations"
        params = {
            "ids[]": idlist,
            "country": country,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def add_organization(self, contest_id: Union[str, int], organization_data: dict,
                         strict: bool = False) -> TeamAffiliation:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/organizations"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, json=organization_data)
        response.raise_for_status()
        return response.json()

    def get_organization(self, contest_id: Union[str, int], organization_id: str,
                         strict: bool = False) -> TeamAffiliation:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/organizations/{organization_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_organization_logo(self, contest_id: Union[str, int], organization_id: str,
                              strict: bool = False) -> bytes:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/organizations/{organization_id}/logo"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.content

    def set_organization_logo(self, contest_id: Union[str, int], organization_id: str, logo: bytes,
                              strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/organizations/{organization_id}/logo"
        params = {
            "strict": strict
        }
        files = {
            "logo": logo
        }
        response = self.session.put(url, params=params, files=files)
        response.raise_for_status()

    def delete_organization_logo(self, contest_id: Union[str, int], organization_id: str,
                                 strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/organizations/{organization_id}/logo"
        params = {
            "strict": strict
        }
        response = self.session.delete(url, params=params)
        response.raise_for_status()

    # Scoreboard section
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

    # Run section
    def get_all_runs(self, contest_id: Union[str, int], idlist: List[str] = None, first_id: str = None, last_id: str = None, judging_id: str = None, limit: int = None, strict: bool = False) -> List[JudgingRun]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/runs"
        params = {
            "ids[]": idlist,
            "first_id": first_id,
            "last_id": last_id,
            "judging_id": judging_id,
            "limit": limit,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_run(self, contest_id: Union[str, int], run_id: str, strict: bool = False) -> JudgingRun:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/runs/{run_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Submission section
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

    def add_submission(self, contest_id: Union[str, int], submission_data: dict, strict: bool = False) -> str:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/submissions"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, files=submission_data)
        response.raise_for_status()
        return response.json()

    def update_submission(self, contest_id: Union[str, int], submission_id: str, submission_data: dict, strict: bool = False) -> str:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/submissions/{submission_id}"
        params = {
            "strict": strict
        }
        response = self.session.put(url, params=params, json=submission_data)
        response.raise_for_status()
        return response.json()

    # Teams section
    def get_all_teams(self, contest_id: Union[str, int], idlist: List[str] = None, category: str = None, affiliation: str = None, public: bool = None, strict: bool = False) -> List[Team]:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/teams"
        params = {
            "ids[]": idlist,
            "category": category,
            "affiliation": affiliation,
            "public": public,
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_team(self, contest_id: Union[str, int], team_id: str, strict: bool = False) -> Team:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/teams/{team_id}"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def add_team(self, contest_id: Union[str, int], team_data: dict, strict: bool = False) -> Team:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/teams"
        params = {
            "strict": strict
        }
        response = self.session.post(url, params=params, json=team_data)
        response.raise_for_status()
        return response.json()

    def update_team(self, contest_id: Union[str, int], team_id: str, team_data: dict, strict: bool = False) -> Team:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/teams/{team_id}"
        params = {
            "strict": strict
        }
        response = self.session.put(url, params=params, json=team_data)
        response.raise_for_status()
        return response.json()

    def delete_team(self, contest_id: Union[str, int], team_id: str, strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/teams/{team_id}"
        params = {
            "strict": strict
        }
        response = self.session.delete(url, params=params)
        response.raise_for_status()

    def get_team_photo(self, contest_id: Union[str, int], team_id: str, strict: bool = False) -> bytes:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/teams/{team_id}/photo"
        params = {
            "strict": strict
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.content

    def set_team_photo(self, contest_id: Union[str, int], team_id: str, photo: bytes, strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/teams/{team_id}/photo"
        params = {
            "strict": strict
        }
        files = {
            "photo": photo
        }
        response = self.session.put(url, params=params, files=files)
        response.raise_for_status()

    def delete_team_photo(self, contest_id: Union[str, int], team_id: str, strict: bool = False) -> None:
        url = f"{self.base_url}/api/v4/contests/{contest_id}/teams/{team_id}/photo"
        params = {
            "strict": strict
        }
        response = self.session.delete(url, params=params)
        response.raise_for_status()

    # Users section
    def get_all_users(self, idlist: List[str] = None, team_id: str = None) -> List[User]:
        url = f"{self.base_url}/api/v4/users"
        params = {
            "ids[]": idlist,
            "team_id": team_id
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_user(self, user_id: str) -> User:
        url = f"{self.base_url}/api/v4/users/{user_id}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def add_user(self, user_data: dict) -> User:
        url = f"{self.base_url}/api/v4/users"
        response = self.session.post(url, json=user_data)
        response.raise_for_status()
        return response.json()

    def update_user(self, user_id: str, user_data: dict) -> User:
        url = f"{self.base_url}/api/v4/users/{user_id}"
        response = self.session.put(url, json=user_data)
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_id: str) -> None:
        url = f"{self.base_url}/api/v4/users/{user_id}"
        response = self.session.delete(url)
        response.raise_for_status()

    def add_groups(self, groups_data: dict) -> dict:
        url = f"{self.base_url}/api/v4/users/groups"
        response = self.session.post(url, files=groups_data)
        response.raise_for_status()
        return response.json()

    def add_organizations(self, organizations_data: dict) -> dict:
        url = f"{self.base_url}/api/v4/users/organizations"
        response = self.session.post(url, files=organizations_data)
        response.raise_for_status()
        return response.json()

    def add_teams(self, teams_data: dict) -> dict:
        url = f"{self.base_url}/api/v4/users/teams"
        response = self.session.post(url, files=teams_data)
        response.raise_for_status()
        return response.json()

    def add_accounts(self, accounts_data: dict) -> dict:
        url = f"{self.base_url}/api/v4/users/accounts"
        response = self.session.post(url, files=accounts_data)
        response.raise_for_status()
        return response.json()
