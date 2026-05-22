"""
QA Pulse by SK — Selenium Boilerplate
test_home.py — home page E2E tests
"""
import pytest
from src.pages.home_page import HomePage


@pytest.mark.smoke
@pytest.mark.e2e
class TestHome:

    def test_home_page_loads(self, home_page: HomePage):
        """Home page loads with correct title."""
        home_page.open_home()
        assert "internet" in home_page.get_title().lower()

    def test_home_page_has_heading(self, home_page: HomePage):
        """Home page has a heading."""
        home_page.open_home()
        assert home_page.get_heading() != ""

    @pytest.mark.regression
    def test_home_page_has_nav_links(self, home_page: HomePage):
        """Home page has more than 10 navigation links."""
        home_page.open_home()
        assert home_page.get_nav_link_count() > 10

    @pytest.mark.regression
    def test_nav_includes_form_auth(self, home_page: HomePage):
        """Form Authentication link is present."""
        home_page.open_home()
        assert home_page.is_link_present("Form Authentication")

    @pytest.mark.regression
    def test_nav_includes_drag_drop(self, home_page: HomePage):
        """Drag and Drop link is present."""
        home_page.open_home()
        assert home_page.is_link_present("Drag and Drop")

    def test_home_page_url(self, home_page: HomePage):
        """Home page URL is correct."""
        home_page.open_home()
        assert "the-internet.herokuapp.com" in home_page.get_url()

    @pytest.mark.regression
    def test_navigate_to_login(self, home_page: HomePage):
        """Clicking Form Authentication navigates to login page."""
        home_page.open_home()
        home_page.click_link("Form Authentication")
        assert "/login" in home_page.get_url()
