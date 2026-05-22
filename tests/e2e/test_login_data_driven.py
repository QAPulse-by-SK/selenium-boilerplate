"""
QA Pulse by SK — Selenium Boilerplate
test_login_data_driven.py — data-driven login tests
"""
from __future__ import annotations

import json
import os

import pytest
from src.pages.login_page import LoginPage
from src.constants.constants import Credentials


def load_users():
    path = os.path.join(os.path.dirname(__file__), "../../test-data/users.json")
    with open(path) as f:
        return json.load(f)


@pytest.mark.regression
@pytest.mark.e2e
@pytest.mark.parametrize("user", load_users())
def test_login_data_driven(driver, user):
    """Data-driven login — reads from test-data/users.json."""
    page = LoginPage(driver)
    page.login(user["username"], user["password"])
    if user["expected"] == "success":
        assert page.is_login_successful()
        assert "You logged into" in page.get_flash_message()
    else:
        assert not page.is_login_successful()


@pytest.mark.smoke
@pytest.mark.e2e
@pytest.mark.parametrize("username,password,should_pass", [
    (Credentials.VALID_USERNAME,   Credentials.VALID_PASSWORD,   True),
    (Credentials.INVALID_USERNAME, Credentials.VALID_PASSWORD,   False),
    (Credentials.VALID_USERNAME,   Credentials.INVALID_PASSWORD, False),
    ("",                           "",                           False),
])
def test_login_parametrize(driver, username, password, should_pass):
    """Parametrized login test — inline data."""
    page = LoginPage(driver)
    page.login(username, password)
    assert page.is_login_successful() == should_pass
