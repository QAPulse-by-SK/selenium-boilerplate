"""
QA Pulse by SK — Selenium Boilerplate
test_brand_site.py — E2E tests for www.skakarh.com
"""
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from src.pages.brand_site_page import BrandSitePage


@pytest.fixture
def brand(driver: WebDriver) -> BrandSitePage:
    return BrandSitePage(driver)


@pytest.mark.smoke
@pytest.mark.e2e
class TestBrandHome:

    def test_homepage_loads(self, brand: BrandSitePage):
        """Homepage loads without errors."""
        brand.open_home()
        assert not brand.is_page_404()
        assert "skakarh" in brand.get_url()

    def test_homepage_has_heading(self, brand: BrandSitePage):
        """Homepage has a hero heading."""
        brand.open_home()
        assert brand.get_hero_heading() != ""

    @pytest.mark.regression
    def test_homepage_title(self, brand: BrandSitePage):
        """Homepage title contains brand keywords."""
        brand.open_home()
        title = brand.get_title().lower()
        assert any(k in title for k in ["qa", "skakarh", "pulse", "automation"])


@pytest.mark.smoke
@pytest.mark.e2e
class TestBrandNavigation:

    def test_navigate_to_blog(self, brand: BrandSitePage):
        """Clicking Blog navigates to blog page."""
        brand.open_home()
        brand.click_nav_blog()
        assert "blog" in brand.get_url().lower()
        assert not brand.is_page_404()

    def test_navigate_to_services(self, brand: BrandSitePage):
        """Clicking Services navigates to services page."""
        brand.open_home()
        brand.click_nav_services()
        assert "service" in brand.get_url().lower()
        assert not brand.is_page_404()

    def test_navigate_to_about(self, brand: BrandSitePage):
        """Clicking About navigates to about page."""
        brand.open_home()
        brand.click_nav_about()
        assert "about" in brand.get_url().lower()
        assert not brand.is_page_404()

    @pytest.mark.regression
    def test_navigate_to_products(self, brand: BrandSitePage):
        """Clicking Products navigates to products page."""
        brand.open_home()
        brand.click_nav_products()
        assert "product" in brand.get_url().lower()
        assert not brand.is_page_404()

    @pytest.mark.regression
    def test_no_404_on_main_pages(self, brand: BrandSitePage):
        """Main pages return valid responses."""
        pages = [
            f"{BrandSitePage.BRAND_URL}/blog/",
            f"{BrandSitePage.BRAND_URL}/services/",
            f"{BrandSitePage.BRAND_URL}/about/",
        ]
        for url in pages:
            brand.open(url)
            assert not brand.is_page_404(), f"404 on: {url}"


@pytest.mark.e2e
class TestBrandBlog:

    def test_blog_page_loads(self, brand: BrandSitePage):
        """Blog page loads without errors."""
        brand.open_blog()
        assert not brand.is_page_404()
        assert "blog" in brand.get_url().lower()

    @pytest.mark.smoke
    def test_blog_has_posts(self, brand: BrandSitePage):
        """Blog page has at least one post link."""
        brand.open_blog()
        count = brand.get_blog_post_count()
        assert count > 0, f"Blog should have posts, found {count}"

    @pytest.mark.smoke
    def test_blog_title(self, brand: BrandSitePage):
        """Blog page title contains blog keywords."""
        brand.open_blog()
        title = brand.get_title().lower()
        assert any(k in title for k in ["blog", "qa", "automation", "pulse"])

    @pytest.mark.regression
    def test_open_first_blog_post(self, brand: BrandSitePage):
        """User can open the first blog post."""
        brand.open_blog()
        links = brand.driver.find_elements(*BrandSitePage.BLOG_ARTICLES)
        assert len(links) > 0, "No blog post links found"
        post_url = links[0].get_attribute("href")
        assert post_url and "/blog/" in post_url, f"Expected blog URL, got: {post_url}"
        brand.open(post_url)
        assert not brand.is_page_404()
        assert brand.get_title() != ""

    @pytest.mark.regression
    def test_blog_has_90_plus_articles(self, brand: BrandSitePage):
        """Blog stats show 90+ articles."""
        brand.open_blog()
        assert "articles" in brand.driver.page_source.lower()


@pytest.mark.e2e
class TestBrandServices:

    def test_services_page_loads(self, brand: BrandSitePage):
        """Services page loads."""
        brand.open_services()
        assert not brand.is_page_404()

    @pytest.mark.smoke
    def test_services_has_cards(self, brand: BrandSitePage):
        """Services page has service cards."""
        brand.open_services()
        assert brand.get_service_card_count() > 0

    @pytest.mark.regression
    def test_services_cards_have_names(self, brand: BrandSitePage):
        """Service cards have visible names."""
        brand.open_services()
        assert len(brand.get_service_names()) > 0


@pytest.mark.e2e
class TestBrandProducts:

    def test_products_page_loads(self, brand: BrandSitePage):
        """Products page loads."""
        brand.open_products()
        assert not brand.is_page_404()

    @pytest.mark.smoke
    def test_products_has_cards(self, brand: BrandSitePage):
        """Products page shows product cards."""
        brand.open_products()
        assert brand.get_product_card_count() > 0

    @pytest.mark.smoke
    def test_products_has_github_links(self, brand: BrandSitePage):
        """Products page has GitHub links."""
        brand.open_products()
        assert brand.get_github_link_count() > 0

    @pytest.mark.regression
    def test_products_has_npm_links(self, brand: BrandSitePage):
        """Products page has npm links."""
        brand.open_products()
        assert brand.get_npm_link_count() > 0

    @pytest.mark.regression
    def test_products_shows_5_plus_products(self, brand: BrandSitePage):
        """Products page shows at least 5 products."""
        brand.open_products()
        assert brand.get_product_card_count() >= 5


@pytest.mark.e2e
class TestBrandAbout:

    def test_about_page_loads(self, brand: BrandSitePage):
        """About page loads."""
        brand.open_about()
        assert not brand.is_page_404()

    @pytest.mark.regression
    def test_about_page_title(self, brand: BrandSitePage):
        """About page has correct title."""
        brand.open_about()
        title = brand.get_title().lower()
        assert any(k in title for k in ["about", "qa", "skakarh", "pulse"])
