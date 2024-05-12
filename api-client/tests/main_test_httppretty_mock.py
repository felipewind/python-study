import httpretty
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@httpretty.activate
def test_read_item():
    # Mocking the external API call
    httpretty.register_uri(
        httpretty.GET,
        "http://localhost:8010/items/1",
        body='{"name": "Sample Item", "price": 100.0, "is_offer": null}',
        content_type="application/json"
    )

    # Call the endpoint
    response = client.get("/items/1")

    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "name": "Sample Item",
        "price": 100.0,
        "is_offer": None
    }
