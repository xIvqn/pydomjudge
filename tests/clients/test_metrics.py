import pytest
import responses
from pydomjudge.domjudge import DOMJudge

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")

@responses.activate
def test_get_metrics(api_client):
    mock_data = "metrics data"
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/metrics/prometheus",
        body=mock_data,
        status=200
    )

    result = api_client.get_metrics()
    assert result == mock_data
