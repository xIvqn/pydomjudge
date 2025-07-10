import pytest
import responses
from pydomjudge import DOMJudge
from pydomjudge.models.main import Team

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")

@responses.activate
def test_get_all_teams(api_client):
    mock_data = [{
        "organization_id": "org1",
        "hidden": False,
        "group_ids": ["group1"],
        "affiliation": "Test Affiliation",
        "nationality": "Test Nationality",
        "id": "1",
        "icpc_id": "icpc1",
        "name": "Test Team",
        "display_name": "Test Team Display",
        "public_description": "This is a test team.",
        "photo": [{
            "href": "http://example.com/photo.jpg",
            "mime": "image/jpeg",
            "hash": "abc123",
            "filename": "photo.jpg",
            "width": 100,
            "height": 100
        }]
    }]
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/teams",
        json=mock_data,
        status=200
    )

    result = api_client.get_all_teams(contest_id="1")
    assert len(result) == 1
    assert isinstance(result[0], Team)
    assert result[0].name == "Test Team"

@responses.activate
def test_get_team(api_client):
    mock_data = {
        "organization_id": "org1",
        "hidden": False,
        "group_ids": ["group1"],
        "affiliation": "Test Affiliation",
        "nationality": "Test Nationality",
        "id": "1",
        "icpc_id": "icpc1",
        "name": "Test Team",
        "display_name": "Test Team Display",
        "public_description": "This is a test team.",
        "photo": [{
            "href": "http://example.com/photo.jpg",
            "mime": "image/jpeg",
            "hash": "abc123",
            "filename": "photo.jpg",
            "width": 100,
            "height": 100
        }]
    }
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/contests/1/teams/1",
        json=mock_data,
        status=200
    )

    result = api_client.get_team(contest_id="1", team_id="1")
    assert isinstance(result, Team)
    assert result.name == "Test Team"

@responses.activate
def test_add_team(api_client):
    mock_data = {
        "organization_id": "org1",
        "hidden": False,
        "group_ids": ["group1"],
        "affiliation": "Test Affiliation",
        "nationality": "Test Nationality",
        "id": "1",
        "icpc_id": "icpc1",
        "name": "Test Team",
        "display_name": "Test Team Display",
        "public_description": "This is a test team.",
        "photo": [{
            "href": "http://example.com/photo.jpg",
            "mime": "image/jpeg",
            "hash": "abc123",
            "filename": "photo.jpg",
            "width": 100,
            "height": 100
        }]
    }
    responses.add(
        responses.POST,
        "http://mock-server/api/v4/contests/1/teams",
        json=mock_data,
        status=201
    )

    team_data = {"name": "Test Team"}
    result = api_client.add_team(contest_id="1", team_data=team_data)
    assert isinstance(result, Team)
    assert result.name == "Test Team"

@responses.activate
def test_update_team(api_client):
    mock_data = {
        "organization_id": "org1",
        "hidden": False,
        "group_ids": ["group1"],
        "affiliation": "Test Affiliation",
        "nationality": "Test Nationality",
        "id": "1",
        "icpc_id": "icpc1",
        "name": "Updated Team",
        "display_name": "Test Team Display",
        "public_description": "This is a test team.",
        "photo": [{
            "href": "http://example.com/photo.jpg",
            "mime": "image/jpeg",
            "hash": "abc123",
            "filename": "photo.jpg",
            "width": 100,
            "height": 100
        }]
    }
    responses.add(
        responses.PUT,
        "http://mock-server/api/v4/contests/1/teams/1",
        json=mock_data,
        status=200
    )

    team_data = {"name": "Updated Team"}
    result = api_client.update_team(contest_id="1", team_id="1", team_data=team_data)
    assert isinstance(result, Team)
    assert result.name == "Updated Team"

@responses.activate
def test_delete_team(api_client):
    responses.add(
        responses.DELETE,
        "http://mock-server/api/v4/contests/1/teams/1",
        status=204
    )

    api_client.delete_team(contest_id="1", team_id="1")
    assert responses.calls[0].request.method == responses.DELETE
