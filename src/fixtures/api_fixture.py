"""
QA Pulse by SK — Selenium Boilerplate
src/fixtures/api_fixture.py — API fixtures

Python equivalent of Playwright's apiFixture.ts.

Usage:
    from src.fixtures.api_fixture import ApiFixtures

    @pytest.fixture
    def api(api_client) -> ApiFixtures:
        return ApiFixtures.create(api_client)

    def test_posts(api: ApiFixtures):
        response = api.posts.get_all()
        assert response.status_code == 200
"""
from __future__ import annotations

from dataclasses import dataclass

from src.api.api_client import ApiClient


class PostsApi:
    """Posts endpoint wrapper."""
    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def get_all(self):
        return self._client.get("/posts")

    def get_by_id(self, post_id: int):
        return self._client.get(f"/posts/{post_id}")

    def create(self, data: dict):
        return self._client.post("/posts", json=data)

    def update(self, post_id: int, data: dict):
        return self._client.put(f"/posts/{post_id}", json=data)

    def delete(self, post_id: int):
        return self._client.delete(f"/posts/{post_id}")


class UsersApi:
    """Users endpoint wrapper."""
    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def get_all(self):
        return self._client.get("/users")

    def get_by_id(self, user_id: int):
        return self._client.get(f"/users/{user_id}")


class CommentsApi:
    """Comments endpoint wrapper."""
    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def get_all(self):
        return self._client.get("/comments")

    def get_by_post(self, post_id: int):
        return self._client.get(f"/posts/{post_id}/comments")


@dataclass
class ApiFixtures:
    """
    Single container for all API endpoint wrappers.

    Usage:
        def test_posts_crud(api: ApiFixtures):
            response = api.posts.get_by_id(1)
            assert response.status_code == 200
            assert response.json()["id"] == 1
    """
    posts:    PostsApi
    users:    UsersApi
    comments: CommentsApi

    @classmethod
    def create(cls, client: ApiClient) -> "ApiFixtures":
        return cls(
            posts    = PostsApi(client),
            users    = UsersApi(client),
            comments = CommentsApi(client),
        )
