import pytest
import responses
from pydomjudge.domjudge import DOMJudge
from pydomjudge.models.response import AccessInformation

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")


@responses.activate
def test_get_access_information_success(api_client):
    # Mock response
    mock_data = {
        "capabilities": [
            "string"
        ],
        "endpoints": [
            {
            "type": "string",
            "properties": [
                "string"
            ]
            }
        ],
    }

    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/access",
        json=mock_data,
        status=200
    )

    # Test
    result = api_client.get_access_information(contest_id=1)

    # Assertions
    assert isinstance(result, AccessInformation)
    assert len(result.capabilities) == 1
    assert len(result.endpoints) == 1


@responses.activate
def test_get_access_information_error(api_client):
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/access",
        json={"error": "Unauthorized"},
        status=401
    )

    with pytest.raises(Exception) as exc_info:
        api_client.get_access_information(contest_id=1)

    assert "401 Client Error" in str(exc_info.value)