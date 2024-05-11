from fastapi.testclient import TestClient
import pytest
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)


@pytest.fixture
def mock_requests_get():
    # Create a MagicMock object to mock requests.get
    with patch('requests.get') as mock_get:
        # Prepare a mock response object with necessary methods
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "name": "Sample Item",
            "price": 100.0,
            "is_offer": None
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response
        yield mock_get


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item(mock_requests_get):
    # The mock_requests_get fixture is automatically used here.
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Sample Item",
        "price": 100.0,
        "is_offer": None
    }
    # Assert if requests.get was called correctly
    mock_requests_get.assert_called_once_with(
        "http://localhost:8010/items/1",
        params={'q': None}
    )
