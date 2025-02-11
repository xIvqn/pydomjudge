import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )

@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    # Configurar entorno para tests
    monkeypatch.setenv("TEST_API_URL", "http://localhost/domjudge")
    monkeypatch.setenv("TEST_API_USER", "testuser")
    monkeypatch.setenv("TEST_API_PASS", "testpass")