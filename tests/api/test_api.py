"""
QA Pulse by SK — Selenium Boilerplate
test_api.py — API tests using ApiClient
"""
import pytest
from src.api.api_client import ApiClient


@pytest.mark.api
class TestApi:

    def test_get_posts_returns_200(self, api_client: ApiClient):
        """GET /posts returns 200."""
        assert api_client.get("/posts").status_code == 200

    def test_get_posts_returns_100(self, api_client: ApiClient):
        """GET /posts returns 100 posts."""
        body = api_client.get("/posts").json()
        assert isinstance(body, list) and len(body) == 100

    def test_get_single_post(self, api_client: ApiClient):
        """GET /posts/1 returns correct post."""
        response = api_client.get("/posts/1")
        body     = response.json()
        assert response.status_code == 200
        assert body["id"] == 1
        assert isinstance(body["title"], str)

    @pytest.mark.smoke
    def test_create_post(self, api_client: ApiClient):
        """POST /posts creates a new post."""
        response = api_client.post("/posts", json={"userId": 1, "title": "QA Pulse by SK", "body": "Test"})
        assert response.status_code == 201
        assert "id" in response.json()

    def test_update_post(self, api_client: ApiClient):
        """PUT /posts/1 updates a post."""
        response = api_client.put("/posts/1", json={"id": 1, "userId": 1, "title": "Updated", "body": "Updated body"})
        assert response.status_code == 200
        assert response.json()["title"] == "Updated"

    def test_delete_post(self, api_client: ApiClient):
        """DELETE /posts/1 returns 200."""
        assert api_client.delete("/posts/1").status_code == 200

    def test_get_users(self, api_client: ApiClient):
        """GET /users returns 10 users."""
        body = api_client.get("/users").json()
        assert len(body) == 10

    @pytest.mark.regression
    def test_response_time_acceptable(self, api_client: ApiClient):
        """API responds within acceptable time."""
        response = api_client.get("/posts/1")
        assert response.elapsed.total_seconds() < 60.0

    @pytest.mark.regression
    def test_content_type_is_json(self, api_client: ApiClient):
        """Response Content-Type is JSON."""
        response = api_client.get("/posts/1")
        assert "application/json" in response.headers.get("Content-Type", "")

    @pytest.mark.regression
    def test_schema_validation(self, api_client: ApiClient):
        """POST schema has required fields with correct types."""
        body = api_client.get("/posts/1").json()
        assert isinstance(body.get("id"),     int)
        assert isinstance(body.get("userId"), int)
        assert isinstance(body.get("title"),  str)
        assert isinstance(body.get("body"),   str)
