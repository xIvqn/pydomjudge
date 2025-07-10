import pytest
import responses
from pydomjudge.domjudge import DOMJudge
from pydomjudge.models.main import Submission

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")

@responses.activate
def test_get_submissions(api_client):
    mock_data = [{
        "language_id": "python",
        "time": "2023-10-01T12:00:00Z",
        "contest_time": "01:00:00",
        "team_id": "team1",
        "problem_id": "problem1",
        "id": "1",
        "external_id": "ext1",
        "entry_point": "main.py",
        "files": [
            {
                "href": "http://mock-server/files/1",
                "mime": "text/plain"
            }
        ]
    }]
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/submissions",
        json=mock_data,
        status=200
    )

    result = api_client.get_submissions(contest_id="1")
    assert len(result) == 1
    assert isinstance(result[0], Submission)
    assert result[0].language_id == "python"

@responses.activate
def test_get_submission(api_client):
    mock_data = {
        "language_id": "python",
        "time": "2023-10-01T12:00:00Z",
        "contest_time": "01:00:00",
        "team_id": "team1",
        "problem_id": "problem1",
        "id": "1",
        "external_id": "ext1",
        "entry_point": "main.py",
        "files": [
            {
                "href": "http://mock-server/files/1",
                "mime": "text/plain"
            }
        ]
    }
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/submissions/1",
        json=mock_data,
        status=200
    )

    result = api_client.get_submission(contest_id="1", submission_id="1")
    assert isinstance(result, Submission)
    assert result.language_id == "python"

@responses.activate
def test_get_submission_files(api_client):
    mock_data = b'file content'
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/submissions/1/files",
        body=mock_data,
        status=200
    )

    result = api_client.get_submission_files(contest_id="1", submission_id="1")
    assert result == mock_data

@responses.activate
def test_get_submission_source_code(api_client):
    mock_data = [{
        "id": "1",
        "submission_id": "1",
        "filename": "main.py",
        "source": "cHJpbnQoJ0hlbGxvLCB3b3JsZCEnKQ=="
    }]
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/submissions/1/source-code",
        json=mock_data,
        status=200
    )

    result = api_client.get_submission_source_code(contest_id="1", submission_id="1")
    assert len(result) == 1
    assert result[0].filename == "main.py"

@responses.activate
def test_add_submission(api_client):
    mock_data = "submission_id"
    responses.add(
        responses.POST,
        "http://mock-server/api/v4/contests/1/submissions",
        json=mock_data,
        status=201
    )

    submission_data = {"file": "content"}
    result = api_client.add_submission(contest_id="1", submission_data=submission_data)
    assert result == mock_data

@responses.activate
def test_update_submission(api_client):
    mock_data = "updated_submission"
    responses.add(
        responses.PUT,
        "http://mock-server/api/v4/contests/1/submissions/1",
        json=mock_data,
        status=200
    )

    submission_data = {"file": "new content"}
    result = api_client.update_submission(contest_id="1", submission_id="1", submission_data=submission_data)
    assert result == mock_data
