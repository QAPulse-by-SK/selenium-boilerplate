"""
QA Pulse by SK — Selenium Boilerplate
src/fixtures/page_fixture.py — Page Object fixtures

Python equivalent of Playwright's pageFixture.ts.
All page objects in one place — single import for test files.

Usage:
    # In conftest.py or test files:
    from src.fixtures.page_fixture import PageFixtures

    # Or use directly in conftest.py fixtures:
    @pytest.fixture
    def pages(driver) -> PageFixtures:
        return PageFixtures(driver)

    def test_login(pages):
        pages.login.login("tomsmith", "SuperSecretPassword!")
        assert pages.secure.is_logged_in()
"""
from __future__ import annotations

from dataclasses import dataclass

from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.secure_page import SecurePage
from src.pages.brand_site_page import BrandSitePage


@dataclass
class PageFixtures:
    """
    Single container for all page objects.
    Instantiated once per test via the `pages` fixture.

    Usage:
        def test_full_flow(pages: PageFixtures):
            pages.home.open_home()
            pages.login.login("tomsmith", "SuperSecretPassword!")
            assert pages.secure.is_logged_in()
            pages.brand.open_blog()
    """
    login:  LoginPage
    home:   HomePage
    secure: SecurePage
    brand:  BrandSitePage

    @classmethod
    def create(cls, driver: WebDriver) -> "PageFixtures":
        """Factory method — creates all page objects from a single driver."""
        return cls(
            login  = LoginPage(driver),
            home   = HomePage(driver),
            secure = SecurePage(driver),
            brand  = BrandSitePage(driver),
        )
