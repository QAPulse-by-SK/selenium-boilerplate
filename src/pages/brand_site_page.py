"""
QA Pulse by SK — Selenium Boilerplate
BrandSitePage — page object for www.skakarh.com
"""
from __future__ import annotations

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage


class BrandSitePage(BasePage):

    BRAND_URL = "https://www.skakarh.com"

    # ── Navigation ────────────────────────────────────────────────────────────
    NAV_BLOG     = (By.LINK_TEXT, "Blog")
    NAV_SERVICES = (By.LINK_TEXT, "Services")
    NAV_PRODUCTS = (By.LINK_TEXT, "Products")
    NAV_ABOUT    = (By.LINK_TEXT, "About")

    # ── Home ──────────────────────────────────────────────────────────────────
    HERO_HEADING = (By.CSS_SELECTOR, "h1")

    # ── Blog ──────────────────────────────────────────────────────────────────
    BLOG_POST_ROWS  = (By.CSS_SELECTOR, "a.article-row")
    BLOG_ARTICLES   = (By.CSS_SELECTOR, ".articles-list a, a.article-row")
    BLOG_H1         = (By.CSS_SELECTOR, ".blog-header h1")

    # ── Services ──────────────────────────────────────────────────────────────
    SERVICE_CARDS = (By.CSS_SELECTOR, ".service-card")
    SERVICE_NAMES = (By.CSS_SELECTOR, ".service-name")

    # ── Products ──────────────────────────────────────────────────────────────
    GITHUB_LINKS  = (By.CSS_SELECTOR, "a[href*='github.com/QAPulse']")
    NPM_BADGES    = (By.CSS_SELECTOR, "a[href*='npmjs.com']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def open_home(self) -> "BrandSitePage":
        self.open(self.BRAND_URL)
        return self

    def open_blog(self) -> "BrandSitePage":
        self.open(f"{self.BRAND_URL}/blog/")
        return self

    def open_services(self) -> "BrandSitePage":
        self.open(f"{self.BRAND_URL}/services/")
        return self

    def open_products(self) -> "BrandSitePage":
        self.open(f"{self.BRAND_URL}/products/")
        return self

    def open_about(self) -> "BrandSitePage":
        self.open(f"{self.BRAND_URL}/about/")
        return self

    def click_nav_blog(self) -> "BrandSitePage":
        self.click(self.NAV_BLOG)
        return self

    def click_nav_services(self) -> "BrandSitePage":
        self.click(self.NAV_SERVICES)
        return self

    def click_nav_products(self) -> "BrandSitePage":
        self.click(self.NAV_PRODUCTS)
        return self

    def click_nav_about(self) -> "BrandSitePage":
        self.click(self.NAV_ABOUT)
        return self

    def get_hero_heading(self) -> str:
        return self.get_text(self.HERO_HEADING)

    def get_blog_post_count(self) -> int:
        return len(self.driver.find_elements(*self.BLOG_ARTICLES))

    def get_blog_headings(self) -> List[str]:
        elements = self.driver.find_elements(*self.BLOG_ARTICLES)
        return [el.text.strip() for el in elements if el.text.strip()]

    def click_first_blog_post(self) -> str:
        """Click first blog post link and return URL navigated to."""
        links = self.driver.find_elements(*self.BLOG_ARTICLES)
        if links:
            href = links[0].get_attribute("href")
            links[0].click()
            return href or ""
        return ""

    def get_service_card_count(self) -> int:
        return len(self.driver.find_elements(*self.SERVICE_CARDS))

    def get_service_names(self) -> List[str]:
        return [el.text.strip() for el in self.driver.find_elements(*self.SERVICE_NAMES) if el.text.strip()]

    def get_product_card_count(self) -> int:
        return len(self.driver.find_elements(*self.SERVICE_CARDS))

    def get_product_names(self) -> List[str]:
        return [el.text.strip() for el in self.driver.find_elements(*self.SERVICE_NAMES) if el.text.strip()]

    def get_github_link_count(self) -> int:
        return len(self.driver.find_elements(*self.GITHUB_LINKS))

    def get_npm_link_count(self) -> int:
        return len(self.driver.find_elements(*self.NPM_BADGES))

    def is_page_404(self) -> bool:
        title = self.get_title().lower()
        return "404" in title or "not found" in title
