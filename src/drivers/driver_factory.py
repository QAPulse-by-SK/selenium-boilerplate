"""
QA Pulse by SK — Selenium Boilerplate
Driver Factory — creates WebDriver instances for all supported browsers
"""
from __future__ import annotations

import os
from typing import Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.safari.options import Options as SafariOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.utils.config_reader import ConfigReader
from src.utils.logger import Logger

log = Logger(__name__)


class DriverFactory:
    """
    Creates and configures WebDriver instances for all supported browsers.

    Supports:
    - Chrome (local + headless + remote)
    - Firefox (local + headless + remote)
    - Edge (local + headless + remote)
    - Safari (local only)
    - Remote Grid (Selenium Grid, BrowserStack, Sauce Labs)
    """

    _config = ConfigReader()

    @classmethod
    def get_driver(
        cls,
        browser: Optional[str] = None,
        headless: Optional[bool] = None,
        remote_url: Optional[str] = None,
    ) -> WebDriver:
        """
        Create and return a configured WebDriver instance.

        Args:
            browser:    Browser name (chrome/firefox/edge/safari). Uses config if None.
            headless:   Run headless. Uses config if None.
            remote_url: Remote Grid URL. Uses config if None.

        Returns:
            Configured WebDriver instance.
        """
        browser    = (browser    or os.getenv("BROWSER",   cls._config.get("browser.default", "chrome"))).lower()
        headless   = headless   if headless   is not None else cls._config.get("browser.headless", False)
        remote_url = remote_url or os.getenv("REMOTE_URL", cls._config.get("grid.url",      ""))
        grid_enabled = os.getenv("GRID_ENABLED", str(cls._config.get("grid.enabled", False))).lower() == "true"

        log.info(f"Creating driver: browser={browser}, headless={headless}, grid={grid_enabled}")

        if grid_enabled and remote_url:
            return cls._get_remote_driver(browser, headless, remote_url)

        drivers = {
            "chrome":  cls._get_chrome_driver,
            "firefox": cls._get_firefox_driver,
            "edge":    cls._get_edge_driver,
            "safari":  cls._get_safari_driver,
        }

        if browser not in drivers:
            raise ValueError(f"Unsupported browser: '{browser}'. Supported: {list(drivers.keys())}")

        driver = drivers[browser](headless)
        cls._configure_driver(driver)
        log.info(f"✅ {browser.capitalize()} driver created successfully")
        return driver

    # ── Chrome ────────────────────────────────────────────────────────────────
    @classmethod
    def _get_chrome_driver(cls, headless: bool) -> WebDriver:
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument(f"--window-size={cls._config.get('browser.window_width', 1280)},{cls._config.get('browser.window_height', 720)}")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        })
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    # ── Firefox ───────────────────────────────────────────────────────────────
    @classmethod
    def _get_firefox_driver(cls, headless: bool) -> WebDriver:
        options = FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("dom.push.enabled", False)
        if headless:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    # ── Edge ──────────────────────────────────────────────────────────────────
    @classmethod
    def _get_edge_driver(cls, headless: bool) -> WebDriver:
        options = EdgeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        if headless:
            options.add_argument("--headless=new")
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)

    # ── Safari ────────────────────────────────────────────────────────────────
    @classmethod
    def _get_safari_driver(cls, headless: bool) -> WebDriver:
        if headless:
            log.warning("Safari does not support headless mode — running headed")
        options = SafariOptions()
        return webdriver.Safari(options=options)

    # ── Remote Grid ───────────────────────────────────────────────────────────
    @classmethod
    def _get_remote_driver(cls, browser: str, headless: bool, remote_url: str) -> WebDriver:
        log.info(f"Connecting to remote grid: {remote_url}")
        capabilities = {
            "chrome":  ChromeOptions,
            "firefox": FirefoxOptions,
            "edge":    EdgeOptions,
        }
        if browser not in capabilities:
            raise ValueError(f"Remote grid does not support: {browser}")

        options = capabilities[browser]()
        if headless and browser != "safari":
            options.add_argument("--headless=new")
        return webdriver.Remote(command_executor=remote_url, options=options)

    # ── Driver Config ─────────────────────────────────────────────────────────
    @classmethod
    def _configure_driver(cls, driver: WebDriver) -> None:
        implicit_wait   = int(os.getenv("IMPLICIT_WAIT",     str(cls._config.get("browser.implicit_wait",    10))))
        page_load_timeout = int(os.getenv("PAGE_LOAD_TIMEOUT", str(cls._config.get("browser.page_load_timeout", 60))))
        width  = int(os.getenv("WINDOW_WIDTH",  str(cls._config.get("browser.window_width",  1280))))
        height = int(os.getenv("WINDOW_HEIGHT", str(cls._config.get("browser.window_height", 720))))

        driver.implicitly_wait(implicit_wait)
        driver.set_page_load_timeout(page_load_timeout)
        driver.set_window_size(width, height)
