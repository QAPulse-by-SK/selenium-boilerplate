"""
QA Pulse by SK — Selenium Boilerplate
SecurePage — page object for the secure area after login.
Demonstrates component composition.
"""
from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage
from src.components.components import FlashMessage


class SecurePage(BasePage):
    """
    Page Object for https://the-internet.herokuapp.com/secure
    Demonstrates BaseComponent composition inside a Page Object.
    """

    HEADING     = (By.TAG_NAME,    "h2")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")
    SUB_HEADING = (By.TAG_NAME,    "h4")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        # ── Component composition ──────────────────────────────────────────
        self.flash = FlashMessage(driver)

    def get_heading(self) -> str:
        return self.get_text(self.HEADING)

    def get_sub_heading(self) -> str:
        return self.get_text(self.SUB_HEADING)

    def click_logout(self) -> "SecurePage":
        self.click(self.LOGOUT_LINK)
        try:
            self.wait_for_url("/login", timeout=5)
        except Exception:
            pass
        return self

    def is_logged_in(self) -> bool:
        return "secure" in self.get_url()

    def get_flash_message(self) -> str:
        """Get flash message via FlashMessage component."""
        return self.flash.get_text_content()

    def is_flash_success(self) -> bool:
        return self.flash.is_success()
