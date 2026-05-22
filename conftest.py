"""
QA Pulse by SK — Selenium Boilerplate
conftest.py — pytest fixtures and hooks
"""
from __future__ import annotations

import os
import pytest

from src.utils.config_reader import (
    TEST_USERNAME, TEST_PASSWORD, SCREENSHOT_DIR, BROWSER, HEADLESS
)


# ── CLI Options ───────────────────────────────────────────────────────────────
def pytest_addoption(parser) -> None:
    parser.addoption("--browser",  action="store", default=BROWSER)
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--remote",   action="store", default="")


# ── Driver Fixtures ───────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def driver(request):
    """Function-scoped WebDriver — new browser per test."""
    from src.helpers.driver_factory import create_driver
    browser  = request.config.getoption("--browser", default=BROWSER)
    headless = request.config.getoption("--headless", default=HEADLESS)
    _driver  = create_driver(browser=browser, headless=headless)
    yield _driver
    _driver.quit()


@pytest.fixture(scope="class")
def driver_class(request):
    """Class-scoped WebDriver — one browser for all tests in a class."""
    from src.helpers.driver_factory import create_driver
    _driver = create_driver(browser=BROWSER, headless=HEADLESS)
    request.cls.driver = _driver
    yield _driver
    _driver.quit()


@pytest.fixture(scope="session")
def driver_session():
    """Session-scoped WebDriver — one browser for entire session."""
    from src.helpers.driver_factory import create_driver
    _driver = create_driver(headless=HEADLESS)
    yield _driver
    _driver.quit()


# ── Page Object Fixtures ──────────────────────────────────────────────────────

@pytest.fixture
def login_page(driver):
    from src.pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def home_page(driver):
    from src.pages.home_page import HomePage
    return HomePage(driver)


@pytest.fixture
def secure_page(driver):
    from src.pages.secure_page import SecurePage
    return SecurePage(driver)


@pytest.fixture
def brand(driver):
    from src.pages.brand_site_page import BrandSitePage
    return BrandSitePage(driver)


@pytest.fixture
def pages(driver):
    """
    All page objects in one fixture — single import for test files.
    Usage: def test_flow(pages): pages.login.login(...); pages.secure.is_logged_in()
    """
    from src.fixtures.page_fixture import PageFixtures
    return PageFixtures.create(driver)


@pytest.fixture
def logged_in_driver(driver):
    """Driver with user already logged in."""
    from src.pages.login_page import LoginPage
    LoginPage(driver).login(TEST_USERNAME, TEST_PASSWORD)
    return driver


# ── API Fixtures ──────────────────────────────────────────────────────────────

@pytest.fixture
def api_client():
    from src.api.api_client import ApiClient
    return ApiClient()


@pytest.fixture
def api(api_client):
    """
    All API endpoints in one fixture.
    Usage: def test_posts(api): api.posts.get_all()
    """
    from src.fixtures.api_fixture import ApiFixtures
    return ApiFixtures.create(api_client)


# ── Helper Fixtures ───────────────────────────────────────────────────────────

@pytest.fixture
def screenshot_helper(driver):
    from src.helpers.screenshot_helper import ScreenshotHelper
    return ScreenshotHelper(driver)


@pytest.fixture
def a11y_helper(driver):
    from src.helpers.a11y_helper import A11yHelper
    return A11yHelper(driver)


# ── Hooks ─────────────────────────────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Auto-capture screenshot on test failure."""
    outcome = yield
    report  = outcome.get_result()
    if report.when == "call" and report.failed:
        _driver = item.funcargs.get("driver") or item.funcargs.get("driver_class")
        if _driver:
            try:
                os.makedirs(SCREENSHOT_DIR, exist_ok=True)
                filename = f"{SCREENSHOT_DIR}/{item.name}_FAILED.png"
                _driver.save_screenshot(filename)
            except Exception:
                pass


def pytest_collection_modifyitems(items) -> None:
    """Auto-add markers based on test file location."""
    for item in items:
        path = str(item.fspath)
        if "e2e"           in path: item.add_marker(pytest.mark.e2e)
        if "api"           in path: item.add_marker(pytest.mark.api)
        if "visual"        in path: item.add_marker(pytest.mark.visual)
        if "accessibility" in path: item.add_marker(pytest.mark.a11y)
