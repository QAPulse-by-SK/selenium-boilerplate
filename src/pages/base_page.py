"""
QA Pulse by SK — Selenium Boilerplate
BasePage — all page objects extend this class.
Provides fluent interface, smart waits, screenshot helpers.
"""

from __future__ import annotations

import os
from datetime import datetime
from typing import List, Optional

from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from src.utils.config_reader import BASE_URL, EXPLICIT_WAIT, SCREENSHOT_DIR
from src.utils.logger import logger


class BasePage:
    """
    Base class for all page objects.

    Provides:
        - Smart explicit waits
        - Fluent interface (methods return self)
        - Screenshot helpers
        - Scroll helpers
        - JS execution helpers
        - Accessibility helpers
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver  = driver
        self.wait    = WebDriverWait(driver, EXPLICIT_WAIT)
        self.actions = ActionChains(driver)

    # ── Navigation ────────────────────────────────────────────────────────────

    def open(self, path: str = "") -> "BasePage":
        """Navigate to a URL or path relative to BASE_URL."""
        url = path if path.startswith("http") else f"{BASE_URL}{path}"
        logger.step(f"Navigating to: {url}")
        self.driver.get(url)
        return self

    def get_url(self) -> str:
        return self.driver.current_url

    def get_title(self) -> str:
        return self.driver.title

    def go_back(self) -> "BasePage":
        self.driver.back()
        return self

    def refresh(self) -> "BasePage":
        self.driver.refresh()
        return self

    # ── Finders ───────────────────────────────────────────────────────────────

    def find(self, locator: tuple) -> WebElement:
        """Find element with explicit wait for visibility."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator: tuple) -> WebElement:
        """Find element with explicit wait for clickability."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator: tuple) -> List[WebElement]:
        """Find all elements with explicit wait for presence."""
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def find_present(self, locator: tuple) -> WebElement:
        """Find element in DOM (not necessarily visible)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    # ── Actions ───────────────────────────────────────────────────────────────

    def click(self, locator: tuple) -> "BasePage":
        """Click element — waits for clickability first."""
        element = self.find_clickable(locator)
        logger.step(f"Clicking: {locator}")
        element.click()
        return self

    def click_js(self, locator: tuple) -> "BasePage":
        """Click element via JavaScript — bypasses overlays."""
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def type(self, locator: tuple, text: str, clear: bool = True) -> "BasePage":
        """Type text into an input field."""
        element = self.find(locator)
        if clear:
            element.clear()
        logger.step(f"Typing '{text}' into: {locator}")
        element.send_keys(text)
        return self

    def type_slowly(self, locator: tuple, text: str, clear: bool = True) -> "BasePage":
        """Type text character by character — for dynamic fields."""
        element = self.find(locator)
        if clear:
            element.clear()
        for char in text:
            element.send_keys(char)
        return self

    def clear(self, locator: tuple) -> "BasePage":
        self.find(locator).clear()
        return self

    def press_key(self, locator: tuple, key: str) -> "BasePage":
        """Press a keyboard key on an element."""
        self.find(locator).send_keys(key)
        return self

    def press_enter(self, locator: tuple) -> "BasePage":
        return self.press_key(locator, Keys.ENTER)

    def select_by_text(self, locator: tuple, text: str) -> "BasePage":
        """Select dropdown option by visible text."""
        Select(self.find(locator)).select_by_visible_text(text)
        return self

    def select_by_value(self, locator: tuple, value: str) -> "BasePage":
        """Select dropdown option by value."""
        Select(self.find(locator)).select_by_value(value)
        return self

    def hover(self, locator: tuple) -> "BasePage":
        """Hover over an element."""
        element = self.find(locator)
        self.actions.move_to_element(element).perform()
        return self

    def drag_and_drop(self, source: tuple, target: tuple) -> "BasePage":
        """Drag element from source to target."""
        src = self.find(source)
        tgt = self.find(target)
        self.actions.drag_and_drop(src, tgt).perform()
        return self

    def double_click(self, locator: tuple) -> "BasePage":
        element = self.find(locator)
        self.actions.double_click(element).perform()
        return self

    def right_click(self, locator: tuple) -> "BasePage":
        element = self.find(locator)
        self.actions.context_click(element).perform()
        return self

    # ── Getters ───────────────────────────────────────────────────────────────

    def get_text(self, locator: tuple) -> str:
        return self.find(locator).text.strip()

    def get_value(self, locator: tuple) -> str:
        return self.find(locator).get_attribute("value") or ""

    def get_attribute(self, locator: tuple, attr: str) -> str:
        return self.find(locator).get_attribute(attr) or ""

    def get_all_texts(self, locator: tuple) -> List[str]:
        return [el.text.strip() for el in self.find_all(locator)]

    # ── State checks ──────────────────────────────────────────────────────────

    def is_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_present(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_enabled(self, locator: tuple) -> bool:
        return self.find(locator).is_enabled()

    def is_checked(self, locator: tuple) -> bool:
        return self.find(locator).is_selected()

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self.find(locator).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    # ── Waits ─────────────────────────────────────────────────────────────────

    def wait_for_visible(self, locator: tuple, timeout: int = EXPLICIT_WAIT) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisible(self, locator: tuple, timeout: int = EXPLICIT_WAIT) -> bool:
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_text(self, locator: tuple, text: str, timeout: int = EXPLICIT_WAIT) -> bool:
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_for_url(self, url_fragment: str, timeout: int = EXPLICIT_WAIT) -> bool:
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_fragment)
        )

    def wait_for_title(self, title: str, timeout: int = EXPLICIT_WAIT) -> bool:
        return WebDriverWait(self.driver, timeout).until(
            EC.title_contains(title)
        )

    # ── Scroll ────────────────────────────────────────────────────────────────

    def scroll_to_element(self, locator: tuple) -> "BasePage":
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return self

    def scroll_to_top(self) -> "BasePage":
        self.driver.execute_script("window.scrollTo(0, 0);")
        return self

    def scroll_to_bottom(self) -> "BasePage":
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self

    def scroll_by(self, x: int = 0, y: int = 300) -> "BasePage":
        self.driver.execute_script(f"window.scrollBy({x}, {y});")
        return self

    # ── JavaScript ────────────────────────────────────────────────────────────

    def execute_js(self, script: str, *args):
        return self.driver.execute_script(script, *args)

    def highlight(self, locator: tuple) -> "BasePage":
        """Highlight an element (useful for debugging)."""
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].style.border='3px solid red';", element
        )
        return self

    # ── Alerts ────────────────────────────────────────────────────────────────

    def accept_alert(self) -> "BasePage":
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        return self

    def dismiss_alert(self) -> "BasePage":
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()
        return self

    def get_alert_text(self) -> str:
        self.wait.until(EC.alert_is_present())
        return self.driver.switch_to.alert.text

    # ── Frames ────────────────────────────────────────────────────────────────

    def switch_to_frame(self, locator: tuple) -> "BasePage":
        frame = self.find(locator)
        self.driver.switch_to.frame(frame)
        return self

    def switch_to_default(self) -> "BasePage":
        self.driver.switch_to.default_content()
        return self

    # ── Windows / Tabs ────────────────────────────────────────────────────────

    def switch_to_new_window(self) -> "BasePage":
        """Switch to the most recently opened window/tab."""
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self

    def close_current_window(self) -> "BasePage":
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return self

    # ── Screenshots ───────────────────────────────────────────────────────────

    def take_screenshot(self, name: str = "") -> str:
        """Take a screenshot and return the file path."""
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{ts}.png" if name else f"screenshot_{ts}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        self.driver.save_screenshot(filepath)
        logger.info(f"📸 Screenshot saved: {filepath}")
        return filepath

    def take_element_screenshot(self, locator: tuple, name: str = "") -> str:
        """Take a screenshot of a specific element."""
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{ts}.png" if name else f"element_{ts}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        self.find(locator).screenshot(filepath)
        return filepath
