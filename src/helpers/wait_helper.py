"""
QA Pulse by SK — Selenium Boilerplate
WaitHelper — advanced wait utilities beyond WebDriverWait
"""
from __future__ import annotations

import time
from typing import Callable, Optional, Tuple, TypeVar

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.utils.logger import Logger

log = Logger(__name__)
T = TypeVar("T")


class WaitHelper:
    """
    Advanced wait utilities.

    Usage:
        waiter = WaitHelper(driver)
        waiter.wait_for_ajax()
        waiter.wait_for_page_load()
        waiter.retry(lambda: page.click_button(), retries=3)
    """

    def __init__(self, driver: WebDriver, timeout: int = 30) -> None:
        self.driver  = driver
        self.timeout = timeout
        self.wait    = WebDriverWait(driver, timeout)

    def wait_for_ajax(self, timeout: int = 30) -> None:
        """Wait for all jQuery AJAX calls to complete."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return jQuery.active == 0")
            )
            log.debug("AJAX calls completed")
        except Exception:
            log.debug("No jQuery found or AJAX already complete")

    def wait_for_page_load(self, timeout: int = 60) -> None:
        """Wait for document.readyState to be complete."""
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        log.debug("Page fully loaded")

    def wait_for_angular(self, timeout: int = 30) -> None:
        """Wait for Angular to finish rendering."""
        script = """
            var callback = arguments[arguments.length - 1];
            if (typeof angular !== 'undefined') {
                angular.getTestability(document.body).whenStable(callback);
            } else { callback(); }
        """
        try:
            self.driver.execute_async_script(script)
        except Exception:
            log.debug("Not an Angular app or Angular already stable")

    def wait_for_url_change(self, original_url: str, timeout: int = 30) -> bool:
        """Wait for URL to change from original."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: d.current_url != original_url
            )
        except TimeoutException:
            return False

    def wait_for_element_count(self, locator: Tuple, count: int, timeout: int = 30) -> bool:
        """Wait for exact number of elements to be present."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: len(d.find_elements(*locator)) == count
            )
        except TimeoutException:
            return False

    def wait_for_attribute_value(
        self, locator: Tuple, attribute: str, value: str, timeout: int = 30
    ) -> bool:
        """Wait for element attribute to have specific value."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*locator).get_attribute(attribute) == value
            )
        except TimeoutException:
            return False

    def sleep(self, seconds: float) -> None:
        """Hard sleep — use sparingly, prefer explicit waits."""
        log.warning(f"Hard sleep: {seconds}s — consider using explicit waits instead")
        time.sleep(seconds)

    @staticmethod
    def retry(
        func: Callable[[], T],
        retries: int = 3,
        delay: float = 1.0,
        exceptions: tuple = (Exception,),
    ) -> T:
        """
        Retry a function on failure.

        Usage:
            result = WaitHelper.retry(lambda: page.get_text(locator), retries=3)
        """
        last_exception: Optional[Exception] = None
        for attempt in range(1, retries + 1):
            try:
                return func()
            except exceptions as e:
                last_exception = e
                if attempt < retries:
                    log.warning(f"Attempt {attempt}/{retries} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        raise last_exception  # type: ignore
