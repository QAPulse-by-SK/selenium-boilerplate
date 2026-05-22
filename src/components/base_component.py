"""
QA Pulse by SK — Selenium Boilerplate
BaseComponent — base class for reusable UI components.

Components are self-contained UI elements that can be composed inside Page Objects.
Examples: NavBar, Footer, Modal, DataTable, SearchBar, Notification

Usage:
    class NavBar(BaseComponent):
        LOGO     = (By.CSS_SELECTOR, ".logo")
        NAV_LINKS = (By.CSS_SELECTOR, "nav a")

        def get_links(self) -> List[str]:
            return self.get_all_texts(self.NAV_LINKS)

    # Compose inside a Page Object:
    class HomePage(BasePage):
        def __init__(self, driver):
            super().__init__(driver)
            self.nav = NavBar(driver)
            self.footer = Footer(driver)
"""
from __future__ import annotations

from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.utils.config_reader import EXPLICIT_WAIT
from src.utils.logger import logger


class BaseComponent:
    """
    Base class for reusable UI components.
    All components extend this class.
    """

    def __init__(self, driver: WebDriver, timeout: int = EXPLICIT_WAIT) -> None:
        self.driver = driver
        self.wait   = WebDriverWait(driver, timeout)

    def find(self, locator: tuple) -> WebElement:
        """Wait for element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: tuple) -> List[WebElement]:
        """Wait for all elements to be present and return them."""
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple) -> "BaseComponent":
        """Click an element."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        logger.step(f"Component clicking: {locator}")
        element.click()
        return self

    def get_text(self, locator: tuple) -> str:
        """Get text of an element."""
        return self.find(locator).text.strip()

    def get_all_texts(self, locator: tuple) -> List[str]:
        """Get text of all matching elements."""
        return [el.text.strip() for el in self.find_all(locator)]

    def is_visible(self, locator: tuple, timeout: int = 5) -> bool:
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False
