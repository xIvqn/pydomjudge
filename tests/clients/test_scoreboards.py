import pytest
import responses
from pydomjudge.domjudge import DOMJudge
from pydomjudge.models.response import Scoreboard

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")

@responses.activate
def test_get_scoreboard(api_client):
    mock_data = {
        "event_id": "1",
        "time": "2025-02-16T20:38:47.068Z",
        "contest_time": "2025-02-16T20:38:47.068Z",
        "state": {
            "started": "2025-02-16T20:38:47.068Z",
            "ended": "2025-02-16T20:38:47.068Z",
            "frozen": "2025-02-16T20:38:47.068Z",
            "thawed": "2025-02-16T20:38:47.068Z",
            "finalized": "2025-02-16T20:38:47.068Z",
            "end_of_updates": "2025-02-16T20:38:47.068Z"
        },
        "rows": [
            {
                "rank": 1,
                "team_id": "1",
                "score": {
                    "num_solved": 1,
                    "total_time": 100
                },
                "problems": [
                    {
                        "label": "A",
                        "problem_id": "1",
                        "num_judged": 1,
                        "num_pending": 0,
                        "solved": True,
                        "time": 100,
                        "first_to_solve": True
                    }
                ]
            }
        ]
    }
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/scoreboard",
        json=mock_data,
        status=200
    )

    result = api_client.get_scoreboard(contest_id="1")
    assert isinstance(result, Scoreboard)
    assert result.event_id == "1"
