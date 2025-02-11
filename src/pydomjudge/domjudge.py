from pydomjudge.clients.teams import TeamsClient
from pydomjudge.clients.users import UsersClient


class DOMJudge(TeamsClient, UsersClient):
    pass