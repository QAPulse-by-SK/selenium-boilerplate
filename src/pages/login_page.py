"""
QA Pulse by SK — Selenium Boilerplate
LoginPage — page object for login page
"""
from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE  = (By.ID, "flash")
    PAGE_HEADING   = (By.TAG_NAME, "h2")
    LOGOUT_LINK    = (By.CSS_SELECTOR, "a[href='/logout']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_login_page(self) -> "LoginPage":
        self.open("/login")
        return self

    def enter_username(self, username: str) -> "LoginPage":
        self.type(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.type(self.PASSWORD_INPUT, password)
        return self

    def click_login(self) -> "LoginPage":
        self.click(self.LOGIN_BUTTON)
        # Wait for either redirect to /secure or flash message to appear
        try:
            self.wait_for_url("/secure", timeout=5)
        except Exception:
            pass  # may stay on login if credentials invalid
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        return (
            self.open_login_page()
                .enter_username(username)
                .enter_password(password)
                .click_login()
        )

    def click_logout(self) -> "LoginPage":
        self.click(self.LOGOUT_LINK)
        try:
            self.wait_for_url("/login", timeout=5)
        except Exception:
            pass
        return self

    def get_flash_message(self) -> str:
        return self.get_text(self.FLASH_MESSAGE)

    def get_heading(self) -> str:
        return self.get_text(self.PAGE_HEADING)

    def is_login_successful(self) -> bool:
        return "secure" in self.get_url()

    def is_flash_visible(self) -> bool:
        return self.is_visible(self.FLASH_MESSAGE)
