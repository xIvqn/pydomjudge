import pytest
import responses
from pydomjudge.domjudge import DOMJudge
from pydomjudge.models.main import JudgingRun

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")

@responses.activate
def test_get_all_runs(api_client):
    mock_data = [{
        "run_time": 0,
        "time": "string",
        "contest_time": "string",
        "judgement_id": "string",
        "ordinal": 0,
        "id": "1",
        "judgement_type_id": "string"
    }]
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/runs",
        json=mock_data,
        status=200
    )

    result = api_client.get_all_runs(contest_id="1")
    assert len(result) == 1
    assert isinstance(result[0], JudgingRun)
    assert result[0].id == "1"

@responses.activate
def test_get_run(api_client):
    mock_data = {
        "run_time": 0,
        "time": "string",
        "contest_time": "string",
        "judgement_id": "string",
        "ordinal": 0,
        "id": "1",
        "judgement_type_id": "string"
    }
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/runs/1",
        json=mock_data,
        status=200
    )

    result = api_client.get_run(contest_id="1", run_id="1")
    assert isinstance(result, JudgingRun)
    assert result.id == "1"
