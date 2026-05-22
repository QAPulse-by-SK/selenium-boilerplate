"""
QA Pulse by SK — Selenium Boilerplate
Wait helpers — custom explicit wait conditions.
"""

from __future__ import annotations

import time
from typing import Callable, Optional

from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    WebDriverException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.utils.config_reader import EXPLICIT_WAIT
from src.utils.logger import logger


def wait_for_condition(
    driver: WebDriver,
    condition: Callable,
    timeout: int = EXPLICIT_WAIT,
    poll: float = 0.5,
    message: str = "Condition not met"
) -> bool:
    """Wait for a custom condition callable to return True."""
    return WebDriverWait(driver, timeout, poll_frequency=poll).until(
        condition, message=message
    )


def wait_for_page_load(driver: WebDriver, timeout: int = EXPLICIT_WAIT) -> None:
    """Wait for document.readyState to be 'complete'."""
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    logger.debug("Page fully loaded")


def wait_for_ajax(driver: WebDriver, timeout: int = EXPLICIT_WAIT) -> None:
    """Wait for jQuery AJAX requests to complete."""
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return jQuery.active") == 0
        )
    except WebDriverException:
        pass  # jQuery not available on page — safe to ignore


def wait_for_element_count(
    driver: WebDriver,
    locator: tuple,
    count: int,
    timeout: int = EXPLICIT_WAIT
) -> bool:
    """Wait until a locator matches exactly N elements."""
    return WebDriverWait(driver, timeout).until(
        lambda d: len(d.find_elements(*locator)) == count
    )


def wait_for_element_count_gte(
    driver: WebDriver,
    locator: tuple,
    min_count: int,
    timeout: int = EXPLICIT_WAIT
) -> bool:
    """Wait until a locator matches at least N elements."""
    return WebDriverWait(driver, timeout).until(
        lambda d: len(d.find_elements(*locator)) >= min_count
    )


def wait_for_url_change(
    driver: WebDriver,
    original_url: str,
    timeout: int = EXPLICIT_WAIT
) -> bool:
    """Wait until the URL changes from the original URL."""
    return WebDriverWait(driver, timeout).until(
        lambda d: d.current_url != original_url
    )


def retry(
    func: Callable,
    retries: int = 3,
    delay: float = 1.0,
    exceptions: tuple = (Exception,)
) -> Callable:
    """
    Retry decorator for flaky operations.

    Usage:
        @retry(retries=3, delay=1.0)
        def click_flaky_button():
            ...
    """
    def wrapper(*args, **kwargs):
        last_exception = None
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                last_exception = e
                logger.warning(f"Retry {attempt + 1}/{retries} — {e}")
                time.sleep(delay)
        raise last_exception
    return wrapper


def sleep(seconds: float) -> None:
    """Explicit sleep — use sparingly, prefer explicit waits."""
    logger.warning(f"⏳ Sleeping {seconds}s — consider using explicit waits instead")
    time.sleep(seconds)
