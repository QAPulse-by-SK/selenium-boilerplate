"""
QA Pulse by SK — Selenium Boilerplate
Example components — NavBar, FlashMessage, DataTable
These demonstrate the BaseComponent pattern.
"""
from __future__ import annotations

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.components.base_component import BaseComponent


class NavBar(BaseComponent):
    """
    Navigation bar component.
    Reusable across any page that has a nav bar.

    Usage:
        nav = NavBar(driver)
        links = nav.get_links()
        nav.click_link("Login")
    """

    LINKS      = (By.CSS_SELECTOR, "nav a, header a, .nav-menu a")
    LOGO       = (By.CSS_SELECTOR, ".logo, .site-logo, header .brand")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def get_links(self) -> List[str]:
        """Get all nav link texts."""
        return self.get_all_texts(self.LINKS)

    def click_link(self, text: str) -> "NavBar":
        """Click a nav link by its text."""
        self.click((By.LINK_TEXT, text))
        return self

    def is_logo_visible(self) -> bool:
        """Check if logo is visible."""
        return self.is_visible(self.LOGO)


class FlashMessage(BaseComponent):
    """
    Flash/notification message component.
    Reusable across any page that shows flash messages.

    Usage:
        flash = FlashMessage(driver)
        text = flash.get_text_content()
        assert flash.is_success()
    """

    CONTAINER = (By.ID,          "flash")
    SUCCESS   = (By.CSS_SELECTOR, ".flash.success, #flash.success, .alert-success")
    ERROR     = (By.CSS_SELECTOR, ".flash.error, #flash.error, .alert-danger")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def get_text_content(self) -> str:
        """Get flash message text."""
        return self.get_text(self.CONTAINER)

    def is_visible(self, locator=None, timeout: int = 5) -> bool:
        """Check if flash message is visible."""
        return super().is_visible(self.CONTAINER, timeout)

    def is_success(self) -> bool:
        """Check if flash message indicates success."""
        text = self.get_text_content().lower()
        return any(k in text for k in ["success", "logged into", "created", "updated"])

    def is_error(self) -> bool:
        """Check if flash message indicates an error."""
        text = self.get_text_content().lower()
        return any(k in text for k in ["invalid", "error", "failed", "incorrect"])


class DataTable(BaseComponent):
    """
    Data table component.
    Reusable for any HTML table.

    Usage:
        table = DataTable(driver, table_id="table1")
        headers = table.get_headers()
        rows = table.get_row_count()
        cell = table.get_cell(row=1, col=2)
    """

    def __init__(self, driver: WebDriver, table_id: str = "table1") -> None:
        super().__init__(driver)
        self._id      = table_id
        self.HEADERS  = (By.CSS_SELECTOR, f"#{table_id} thead th")
        self.ROWS     = (By.CSS_SELECTOR, f"#{table_id} tbody tr")
        self.CELLS    = (By.CSS_SELECTOR, f"#{table_id} tbody td")

    def get_headers(self) -> List[str]:
        """Get all column header texts."""
        return self.get_all_texts(self.HEADERS)

    def get_row_count(self) -> int:
        """Get number of data rows."""
        return len(self.driver.find_elements(*self.ROWS))

    def get_cell(self, row: int, col: int) -> str:
        """Get cell text by 1-based row and column index."""
        cells = self.driver.find_elements(
            By.CSS_SELECTOR, f"#{self._id} tbody tr:nth-child({row}) td"
        )
        if col <= len(cells):
            return cells[col - 1].text.strip()
        return ""

    def has_column(self, column_name: str) -> bool:
        """Check if table has a column with given header text."""
        return column_name in self.get_headers()
