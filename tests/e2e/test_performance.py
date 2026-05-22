"""
QA Pulse by SK — Selenium Boilerplate
test_performance.py — page performance + SLA tests
Uses Chrome DevTools Protocol (CDP) for performance metrics
"""
from __future__ import annotations

import time
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage
from src.pages.brand_site_page import BrandSitePage
from src.constants.constants import URLs


@pytest.mark.regression
@pytest.mark.e2e
class TestPerformance:
    """Page load performance tests — SLA benchmarks."""

    @pytest.mark.parametrize("path,name,sla_ms", [
        ("/",      "home",       5000),
        ("/login", "login",      5000),
        ("/tables","tables",     5000),
    ])
    def test_page_load_within_sla(self, driver: WebDriver, path: str, name: str, sla_ms: int):
        """Pages load within their SLA threshold."""
        page  = BasePage(driver)
        start = time.time()
        page.open(path)
        duration_ms = (time.time() - start) * 1000
        assert duration_ms < sla_ms, (
            f"{name} page took {duration_ms:.0f}ms — exceeds SLA of {sla_ms}ms"
        )

    def test_brand_site_home_load_sla(self, driver: WebDriver):
        """skakarh.com homepage loads within 8 seconds."""
        page  = BrandSitePage(driver)
        start = time.time()
        page.open_home()
        duration_ms = (time.time() - start) * 1000
        assert duration_ms < 8000, f"Homepage took {duration_ms:.0f}ms — exceeds 8000ms SLA"

    def test_api_response_time(self):
        """API responses within 2 seconds."""
        import requests
        start    = time.time()
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        duration = time.time() - start
        assert response.status_code == 200
        assert duration < 2.0, f"API took {duration:.3f}s — exceeds 2s SLA"

    def test_page_load_navigation_timing(self, driver: WebDriver):
        """Collect Navigation Timing API metrics."""
        page = BasePage(driver)
        page.open("/")
        timing = driver.execute_script("""
            const t = window.performance.timing;
            return {
                domComplete: t.domComplete - t.navigationStart,
                loadEvent:   t.loadEventEnd - t.navigationStart,
                ttfb:        t.responseStart - t.navigationStart,
            };
        """)
        print(f"\n  TTFB:        {timing['ttfb']}ms")
        print(f"  DOM Complete:{timing['domComplete']}ms")
        print(f"  Load Event:  {timing['loadEvent']}ms")
        assert timing["loadEvent"] < 10000, "Page load event exceeded 10s"
        assert timing["ttfb"] < 3000, "Time to first byte exceeded 3s"
