"""
QA Pulse by SK — Selenium Boilerplate
ApiClient — base class for API testing with requests.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

import requests
from requests import Response, Session

from src.utils.config_reader import API_BASE_URL
from src.utils.logger import logger


class ApiClient:
    """
    Base API client using requests.
    Handles auth, headers, logging, and response validation.
    """

    def __init__(
        self,
        base_url: str = API_BASE_URL,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 30,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout  = timeout
        self.session  = Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept":       "application/json",
            **(headers or {}),
        })

    def set_auth_token(self, token: str) -> "ApiClient":
        """Set Bearer token for all subsequent requests."""
        self.session.headers["Authorization"] = f"Bearer {token}"
        return self

    def set_header(self, key: str, value: str) -> "ApiClient":
        self.session.headers[key] = value
        return self

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.step(f"GET {url}")
        response = self.session.get(url, params=params, timeout=self.timeout)
        self._log_response(response)
        return response

    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None) -> Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.step(f"POST {url}")
        response = self.session.post(url, data=data, json=json, timeout=self.timeout)
        self._log_response(response)
        return response

    def put(self, endpoint: str, json: Optional[Dict] = None) -> Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.step(f"PUT {url}")
        response = self.session.put(url, json=json, timeout=self.timeout)
        self._log_response(response)
        return response

    def patch(self, endpoint: str, json: Optional[Dict] = None) -> Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.step(f"PATCH {url}")
        response = self.session.patch(url, json=json, timeout=self.timeout)
        self._log_response(response)
        return response

    def delete(self, endpoint: str) -> Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.step(f"DELETE {url}")
        response = self.session.delete(url, timeout=self.timeout)
        self._log_response(response)
        return response

    def assert_status(self, response: Response, expected: int) -> None:
        assert response.status_code == expected, (
            f"Expected status {expected}, got {response.status_code}\n"
            f"Response: {response.text[:500]}"
        )
        logger.pass_(f"Status {response.status_code} ✓")

    def assert_success(self, response: Response) -> None:
        assert 200 <= response.status_code < 300, (
            f"Expected 2xx, got {response.status_code}\n"
            f"Response: {response.text[:500]}"
        )
        logger.pass_(f"Success status {response.status_code} ✓")

    def _log_response(self, response: Response) -> None:
        status = response.status_code
        if status < 400:
            logger.pass_(f"Response: {status}")
        else:
            logger.error(f"Response: {status} — {response.text[:200]}")
