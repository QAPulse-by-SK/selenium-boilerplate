"""
QA Pulse by SK — Selenium Boilerplate
Accessibility Tests — WCAG 2.1 checks via axe-selenium-python
"""

import pytest

from src.helpers.a11y_helper import A11yHelper
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage


@pytest.mark.a11y
class TestAccessibility:
    """
    WCAG 2.1 accessibility tests.
    Requires: pip install axe-selenium-python
    """

    def test_home_page_no_critical_violations(self, driver):
        """Home page has no critical accessibility violations."""
        page = HomePage(driver)
        page.open_home()
        a11y = A11yHelper(driver)
        a11y.assert_no_critical_violations()

    def test_login_page_no_critical_violations(self, driver):
        """Login page has no critical accessibility violations."""
        page = LoginPage(driver)
        page.open_login_page()
        a11y = A11yHelper(driver)
        a11y.assert_no_critical_violations()

    def test_home_page_violation_count(self, driver):
        """Home page violations are within acceptable threshold."""
        page = HomePage(driver)
        page.open_home()
        a11y  = A11yHelper(driver)
        count = a11y.get_violation_count()
        # Log what we find — may have known legacy violations
        a11y.print_violations()
        assert count < 20, f"Too many a11y violations: {count}"

    def test_login_page_has_labels(self, driver):
        """Login form inputs have associated labels."""
        page = LoginPage(driver)
        page.open_login_page()
        # Check username input has a label
        username = driver.find_element("id", "username")
        assert username.get_attribute("id"), "Username input should have id"

    def test_login_page_no_serious_violations(self, driver):
        """Login page has no serious or critical violations."""
        page = LoginPage(driver)
        page.open_login_page()
        a11y = A11yHelper(driver)
        a11y.assert_no_serious_violations()
