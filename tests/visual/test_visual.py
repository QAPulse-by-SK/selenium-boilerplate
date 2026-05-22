"""
QA Pulse by SK — Selenium Boilerplate
test_visual.py — visual regression tests
"""
import pytest
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.helpers.screenshot_helper import ScreenshotHelper


@pytest.mark.visual
class TestVisual:

    def test_home_page_visual(self, home_page: HomePage, screenshot_helper: ScreenshotHelper):
        """Home page matches visual baseline."""
        home_page.open_home()
        passed, diff = screenshot_helper.compare_with_baseline("home_page")
        assert passed, f"Visual diff too high: {diff:.2%}"

    def test_login_page_visual(self, login_page: LoginPage, screenshot_helper: ScreenshotHelper):
        """Login page matches visual baseline."""
        login_page.open_login_page()
        passed, diff = screenshot_helper.compare_with_baseline("login_page")
        assert passed, f"Visual diff too high: {diff:.2%}"
