"""
QA Pulse by SK — Selenium Boilerplate
HomePage — page object for home page
"""
from __future__ import annotations

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage


class HomePage(BasePage):

    HEADING   = (By.TAG_NAME, "h1")
    NAV_LINKS = (By.CSS_SELECTOR, "ul li a")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_home(self) -> "HomePage":
        self.open("/")
        return self

    def get_heading(self) -> str:
        return self.get_text(self.HEADING)

    def get_nav_links(self) -> List[str]:
        return [el.text.strip() for el in self.find_all(self.NAV_LINKS)]

    def get_nav_link_count(self) -> int:
        return len(self.driver.find_elements(*self.NAV_LINKS))

    def click_link(self, link_text: str) -> "HomePage":
        self.click((By.LINK_TEXT, link_text))
        return self

    def is_link_present(self, link_text: str) -> bool:
        return link_text in self.get_nav_links()
