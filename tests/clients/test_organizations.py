import pytest
import responses
from pydomjudge.domjudge import DOMJudge
from pydomjudge.models.main import TeamAffiliation

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")

@responses.activate
def test_get_all_organizations(api_client):
    mock_data = [{"id": "1", "name": "Test Organization", "shortname": "TestOrg", "formal_name": "Test Organization Formal", "icpc_id": None, "country": None}]
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/organizations",
        json=mock_data,
        status=200
    )

    result = api_client.get_all_organizations(contest_id="1")
    assert len(result) == 1
    assert isinstance(result[0], TeamAffiliation)
    assert result[0].name == "Test Organization"

@responses.activate
def test_get_organization(api_client):
    mock_data = {"id": "1", "name": "Test Organization", "shortname": "TestOrg", "formal_name": "Test Organization Formal", "icpc_id": None, "country": None}
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/organizations/1",
        json=mock_data,
        status=200
    )

    result = api_client.get_organization(contest_id="1", organization_id="1")
    assert isinstance(result, TeamAffiliation)
    assert result.name == "Test Organization"

@responses.activate
def test_get_organization_logo(api_client):
    mock_data = b'logo content'
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/organizations/1/logo",
        body=mock_data,
        status=200
    )

    result = api_client.get_organization_logo(contest_id="1", organization_id="1")
    assert result == mock_data

@responses.activate
def test_set_organization_logo(api_client):
    responses.add(
        responses.PUT,
        "http://mock-server/api/v4/contests/1/organizations/1/logo",
        status=200
    )

    api_client.set_organization_logo(contest_id="1", organization_id="1", logo=b'logo content')
    assert responses.calls[0].request.method == responses.PUT

@responses.activate
def test_delete_organization_logo(api_client):
    responses.add(
        responses.DELETE,
        "http://mock-server/api/v4/contests/1/organizations/1/logo",
        status=200
    )

    api_client.delete_organization_logo(contest_id="1", organization_id="1")
    assert responses.calls[0].request.method == responses.DELETE
