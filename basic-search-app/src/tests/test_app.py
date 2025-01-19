import pytest
from app import app

# Create a test client for the Flask app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the home route
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Basic Search App" in response.data

# Test the search route with a valid query
def test_search_valid(client):
    response = client.post("/search", data={"query": "apple"})
    assert response.status_code == 200
    assert b"Results for \"apple\":" in response.data
    assert b"apple" in response.data

# Test the search route with no matching results
def test_search_no_results(client):
    response = client.post("/search", data={"query": "mango"})
    assert response.status_code == 200
    assert b"No results found." in response.data

# Test case-insensitive search
def test_search_case_insensitive(client):
    response = client.post("/search", data={"query": "APPLE"})
    assert response.status_code == 200
    assert b"apple" in response.data

