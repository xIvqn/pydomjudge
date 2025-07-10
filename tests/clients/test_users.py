import pytest
import responses
from pydomjudge.domjudge import DOMJudge
from pydomjudge.models.main import User

@pytest.fixture
def api_client():
    return DOMJudge("http://mock-server", "user", "pass")

@responses.activate
def test_get_all_users(api_client):
    mock_data = [{
            "id": "1",
            "username": "testuser",
            "name": "Test User",
            "email": "testuser@example.com",
            "team_id": "team1",
            "roles": ["team_member"],
            "enabled": True,
            "last_login_time": "2023-10-01T12:00:00Z"
    }]
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/users",
        json=mock_data,
        status=200
    )

    result = api_client.get_all_users()
    assert len(result) == 1
    assert isinstance(result[0], User)
    assert result[0].username == "testuser"

@responses.activate
def test_get_user(api_client):
    mock_data = {
            "id": "1",
            "username": "testuser",
            "name": "Test User",
            "email": "testuser@example.com",
            "team_id": "team1",
            "roles": ["team_member"],
            "enabled": True,
            "last_login_time": "2023-10-01T12:00:00Z"
    }
    responses.add(
        responses.GET,
        "http://mock-server/api/v4/users/1",
        json=mock_data,
        status=200
    )

    result = api_client.get_user(user_id="1")
    assert isinstance(result, User)
    assert result.username == "testuser"

@responses.activate
def test_add_user(api_client):
    mock_data = {
            "id": "1",
            "username": "testuser",
            "name": "Test User",
            "email": "testuser@example.com",
            "team_id": "team1",
            "roles": ["team_member"],
            "enabled": True,
            "last_login_time": "2023-10-01T12:00:00Z"
    }
    responses.add(
        responses.POST,
        "http://mock-server/api/v4/users",
        json=mock_data,
        status=201
    )

    user_data = {"username": "testuser"}
    result = api_client.add_user(user_data=user_data)
    assert isinstance(result, User)
    assert result.username == "testuser"

@responses.activate
def test_update_user(api_client):
    mock_data = {
            "id": "1",
            "username": "updateduser",
            "name": "Test User",
            "email": "testuser@example.com",
            "team_id": "team1",
            "roles": ["team_member"],
            "enabled": True,
            "last_login_time": "2023-10-01T12:00:00Z"
    }
    responses.add(
        responses.PUT,
        "http://mock-server/api/v4/users/1",
        json=mock_data,
        status=200
    )

    user_data = {"username": "updateduser"}
    result = api_client.update_user(user_id="1", user_data=user_data)
    assert isinstance(result, User)
    assert result.username == "updateduser"

@responses.activate
def test_delete_user(api_client):
    responses.add(
        responses.DELETE,
        "http://mock-server/api/v4/users/1",
        status=204
    )

    api_client.delete_user(user_id="1")
    assert responses.calls[0].request.method == responses.DELETE
