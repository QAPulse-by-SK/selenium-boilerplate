"""
QA Pulse by SK — Selenium Boilerplate
WebDriver factory — supports Chrome, Firefox, Edge, Safari
Local + Remote (Selenium Grid / BrowserStack / Sauce Labs)
Uses Selenium 4 built-in driver manager — no webdriver-manager needed.
"""
from __future__ import annotations

from typing import Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.safari.options import Options as SafariOptions

from src.utils.config_reader import (
    BROWSER, EXPLICIT_WAIT, HEADLESS,
    IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT, REMOTE_URL,
)
from src.utils.logger import logger


def create_driver(
    browser:    Optional[str]  = None,
    headless:   Optional[bool] = None,
    remote_url: Optional[str]  = None,
) -> WebDriver:
    """
    Create and return a configured WebDriver instance.

    Args:
        browser:    chrome | firefox | edge | safari
        headless:   Run headless
        remote_url: Remote Selenium Grid URL

    Returns:
        Configured WebDriver instance
    """
    _browser    = (browser    or BROWSER).lower()
    _headless   = headless   if headless   is not None else HEADLESS
    _remote_url = remote_url if remote_url is not None else REMOTE_URL

    logger.info(f"Creating {_browser} driver (headless={_headless})")

    if _remote_url:
        driver = _create_remote_driver(_browser, _headless, _remote_url)
    else:
        driver = _create_local_driver(_browser, _headless)

    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    driver.maximize_window()

    logger.pass_(f"{_browser.capitalize()} driver ready")
    return driver


def _create_local_driver(browser: str, headless: bool) -> WebDriver:
    """Create a local driver using Selenium 4 built-in manager."""
    drivers = {
        "chrome":  _chrome_driver,
        "firefox": _firefox_driver,
        "edge":    _edge_driver,
        "safari":  _safari_driver,
    }
    if browser not in drivers:
        raise ValueError(f"Unsupported browser: '{browser}'. Use: chrome|firefox|edge|safari")
    return drivers[browser](headless)


def _create_remote_driver(browser: str, headless: bool, remote_url: str) -> WebDriver:
    """Create a remote WebDriver (Selenium Grid / BrowserStack / Sauce Labs)."""
    logger.info(f"Connecting to remote Grid: {remote_url}")
    options_map = {
        "chrome":  _chrome_options,
        "firefox": _firefox_options,
        "edge":    _edge_options,
    }
    options = options_map.get(browser, _chrome_options)(headless)
    return webdriver.Remote(command_executor=remote_url, options=options)


# ── Options builders ──────────────────────────────────────────────────────────

def _chrome_options(headless: bool) -> ChromeOptions:
    opts = ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-notifications")
    opts.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)
    return opts


def _firefox_options(headless: bool) -> FirefoxOptions:
    opts = FirefoxOptions()
    if headless:
        opts.add_argument("--headless")
    return opts


def _edge_options(headless: bool) -> EdgeOptions:
    opts = EdgeOptions()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    return opts


# ── Driver creators ───────────────────────────────────────────────────────────

def _chrome_driver(headless: bool) -> WebDriver:
    """Chrome — uses Selenium 4 built-in manager."""
    return webdriver.Chrome(options=_chrome_options(headless))


def _firefox_driver(headless: bool) -> WebDriver:
    """Firefox — uses Selenium 4 built-in manager."""
    return webdriver.Firefox(options=_firefox_options(headless))


def _edge_driver(headless: bool) -> WebDriver:
    """Edge — uses Selenium 4 built-in manager."""
    return webdriver.Edge(options=_edge_options(headless))


def _safari_driver(_headless: bool = False) -> WebDriver:
    """Safari — uses built-in SafariDriver (no manager needed)."""
    return webdriver.Safari(options=SafariOptions())
