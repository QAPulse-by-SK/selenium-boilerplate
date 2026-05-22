"""
QA Pulse by SK — Selenium Boilerplate
test_accessibility.py — WCAG 2.1 accessibility tests
"""
import pytest
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.helpers.a11y_helper import A11yHelper


@pytest.mark.a11y
class TestAccessibility:

    def test_home_page_no_critical_violations(self, home_page: HomePage, a11y_helper: A11yHelper):
        """Home page has no critical accessibility violations."""
        home_page.open_home()
        a11y_helper.assert_no_critical_violations()

    def test_login_page_no_critical_violations(self, login_page: LoginPage, a11y_helper: A11yHelper):
        """Login page has no critical accessibility violations."""
        login_page.open_login_page()
        a11y_helper.assert_no_critical_violations()

    @pytest.mark.regression
    def test_login_page_no_serious_violations(self, login_page: LoginPage, a11y_helper: A11yHelper):
        """Login page has no serious accessibility violations."""
        login_page.open_login_page()
        a11y_helper.assert_no_serious_or_critical()

    def test_home_page_full_analysis(self, home_page: HomePage, a11y_helper: A11yHelper):
        """Full accessibility analysis — only fail on critical."""
        home_page.open_home()
        result = a11y_helper.analyze()
        for v in result.violations:
            print(f"  [{v.impact.upper()}] {v.id}: {v.help}")
        assert result.critical_count == 0, f"Found {result.critical_count} critical violations"
