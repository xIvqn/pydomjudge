import pytest
import responses
from pydomjudge.domjudge import DOMJudge
from pydomjudge.models.main import Language

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")

@responses.activate
def test_get_all_languages(api_client):
    mock_data = [
        {
            "id": "1",
            "name": "Python",
            "extensions": [".py"],
            "compile_executable_hash": None,
            "filter_compiler_files": False,
            "allow_judge": True,
            "time_factor": 1.0,
            "entry_point_required": False,
            "entry_point_name": None
        }
    ]
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/languages",
        json=mock_data,
        status=200
    )

    result = api_client.get_all_languages(contest_id="1")
    assert len(result) == 1
    assert isinstance(result[0], Language)
    assert result[0].name == "Python"

@responses.activate
def test_get_language(api_client):
    mock_data = {
        "id": "1",
        "name": "Python",
        "extensions": [".py"],
        "compile_executable_hash": None,
        "filter_compiler_files": False,
        "allow_judge": True,
        "time_factor": 1.0,
        "entry_point_required": False,
        "entry_point_name": None
    }
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/languages/1",
        json=mock_data,
        status=200
    )

    result = api_client.get_language(contest_id="1", language_id="1")
    assert isinstance(result, Language)
    assert result.name == "Python"
