"""
QA Pulse by SK — Selenium Boilerplate
test_login.py — Login page E2E tests
"""
import pytest
from src.pages.login_page import LoginPage
from src.constants.constants import Credentials


@pytest.mark.smoke
@pytest.mark.e2e
class TestLogin:

    def test_login_page_loads(self, login_page: LoginPage):
        """Login page loads with heading visible."""
        login_page.open_login_page()
        assert login_page.is_visible(LoginPage.PAGE_HEADING)
        assert "login" in login_page.get_heading().lower()

    def test_valid_login(self, login_page: LoginPage):
        """Valid credentials redirect to secure area."""
        login_page.login(Credentials.VALID_USERNAME, Credentials.VALID_PASSWORD)
        assert login_page.is_login_successful()
        assert "logged into" in login_page.get_flash_message().lower()

    def test_invalid_username(self, login_page: LoginPage):
        """Invalid username shows error message."""
        login_page.login(Credentials.INVALID_USERNAME, Credentials.VALID_PASSWORD)
        assert not login_page.is_login_successful()
        assert "invalid" in login_page.get_flash_message().lower()

    def test_invalid_password(self, login_page: LoginPage):
        """Invalid password shows error message."""
        login_page.login(Credentials.VALID_USERNAME, Credentials.INVALID_PASSWORD)
        assert not login_page.is_login_successful()

    def test_empty_credentials(self, login_page: LoginPage):
        """Empty credentials shows error."""
        login_page.login("", "")
        assert not login_page.is_login_successful()

    def test_logout(self, login_page: LoginPage):
        """User can logout after login."""
        login_page.login(Credentials.VALID_USERNAME, Credentials.VALID_PASSWORD)
        assert login_page.is_login_successful()
        login_page.click_logout()
        assert "logged out" in login_page.get_flash_message().lower()

    @pytest.mark.regression
    def test_password_field_is_masked(self, login_page: LoginPage):
        """Password field type is password."""
        login_page.open_login_page()
        assert login_page.get_attribute(LoginPage.PASSWORD_INPUT, "type") == "password"

    @pytest.mark.regression
    def test_login_button_enabled(self, login_page: LoginPage):
        """Login button is enabled on page load."""
        login_page.open_login_page()
        assert login_page.is_enabled(LoginPage.LOGIN_BUTTON)

    @pytest.mark.regression
    def test_flash_visible_after_failed_login(self, login_page: LoginPage):
        """Flash message is visible after failed login."""
        login_page.login("wrong", "wrong")
        assert login_page.is_flash_visible()

    @pytest.mark.regression
    def test_login_url(self, login_page: LoginPage):
        """Login page URL is correct."""
        login_page.open_login_page()
        assert "/login" in login_page.get_url()
