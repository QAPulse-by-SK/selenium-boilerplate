<div align="center">

<img src="https://img.shields.io/badge/QA%20Pulse%20by%20SK-Selenium%20Boilerplate-3b82f6?style=for-the-badge&logoColor=white" height="35"/>

# Selenium Boilerplate

### *Production-grade Selenium test automation — Python · Java · JavaScript*

**Clone. Configure. Start testing.**

<br/>

[![Python Tests](https://github.com/QAPulse-by-SK/selenium-boilerplate/actions/workflows/python.yml/badge.svg)](https://github.com/QAPulse-by-SK/selenium-boilerplate/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12+-3b82f6?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.18-43B02A?style=flat-square&logo=selenium&logoColor=white)](https://selenium.dev)
[![pytest](https://img.shields.io/badge/pytest-8.1-f59e0b?style=flat-square)](https://pytest.org)
[![QA Pulse by SK](https://img.shields.io/badge/QAPulse--by--SK-skakarh.com-3b82f6?style=flat-square)](https://www.skakarh.com)

<br/>

🌐 **[www.skakarh.com](https://www.skakarh.com)** &nbsp;|&nbsp; 📦 **[Products](https://www.skakarh.com/products/)** &nbsp;|&nbsp; 🏢 **[QAPulse-by-SK](https://github.com/QAPulse-by-SK)**

</div>

---

## 🌿 Branch Strategy

| Branch | Language | Framework | Status |
|---|---|---|---|
| `master` | **Python 3.12+** | pytest + Selenium 4 | ✅ Live — 87 tests |
| `java` | Java 17+ | Maven + TestNG + Allure | 🔜 Coming Soon |
| `javascript` | TypeScript | WebdriverIO + Mocha | 🔜 Coming Soon |

All branches are **feature-identical** — same test coverage, same CI/CD, same folder structure. Pick the language your team works in.

---

## ⚡ Quick Start

```bash
# 1 — Clone
git clone https://github.com/QAPulse-by-SK/selenium-boilerplate.git
cd selenium-boilerplate

# 2 — Install dependencies
bash req_scripts/install_requirements.sh

# 3 — Configure
cp .env.example .env

# 4 — Run all tests (headless, parallel)
pytest tests/ --headless -n 2
```

**Requirements:** Python 3.12+ · Chrome / Firefox / Edge / Safari
No manual driver download — Selenium 4 built-in manager handles it automatically.

---

## 📁 Project Structure

```
selenium-boilerplate/
├── src/
│   ├── pages/                      # Page Object Model
│   │   ├── base_page.py            # BasePage — fluent interface + smart waits
│   │   ├── login_page.py           # LoginPage
│   │   ├── home_page.py            # HomePage
│   │   ├── secure_page.py          # SecurePage (post-login) + component composition
│   │   └── brand_site_page.py      # BrandSitePage — www.skakarh.com
│   ├── components/                 # Reusable UI components
│   │   ├── base_component.py       # BaseComponent — base for all components
│   │   └── components.py           # NavBar, FlashMessage, DataTable
│   ├── fixtures/                   # Test fixtures (like Playwright's pageFixture.ts)
│   │   ├── page_fixture.py         # PageFixtures — all pages in one import
│   │   └── api_fixture.py          # ApiFixtures — PostsApi, UsersApi, CommentsApi
│   ├── api/
│   │   └── api_client.py           # requests-based HTTP client
│   ├── helpers/
│   │   ├── driver_factory.py       # Chrome/Firefox/Edge/Safari factory
│   │   ├── wait_helper.py          # Advanced waits + retry decorator
│   │   ├── screenshot_helper.py    # Visual regression with Pillow
│   │   └── a11y_helper.py          # WCAG 2.1 via axe-selenium-python
│   ├── utils/
│   │   ├── logger.py               # Colour-coded logger with timestamps
│   │   ├── config_reader.py        # config.yaml + .env dot-notation access
│   │   └── data_factory.py         # Faker-based test data generation
│   ├── types/
│   │   └── types.py                # Shared dataclasses — User, BrowserConfig, etc.
│   └── constants/
│       └── constants.py            # URLs, Credentials, Timeouts, Tags
├── tests/
│   ├── e2e/
│   │   ├── test_login.py           # 10 tests — valid/invalid login, logout, masking
│   │   ├── test_home.py            # 7 tests  — navigation, links, headings
│   │   ├── test_brand_site.py      # 30 tests — skakarh.com E2E flows
│   │   ├── test_login_data_driven.py  # 8 tests — JSON fixtures + parametrize
│   │   ├── test_advanced_interactions.py  # 22 tests — checkboxes, dropdowns, alerts, drag&drop, windows, hovers, tables
│   │   └── test_performance.py     # Performance + Navigation Timing API
│   ├── api/
│   │   └── test_api.py             # 10 tests — CRUD + schema validation
│   ├── visual/
│   │   └── test_visual.py          # Visual regression with Pillow baselines
│   └── accessibility/
│       └── test_accessibility.py   # WCAG 2.1 AA tests
├── test-data/
│   └── users.json                  # Data-driven test fixtures
├── .github/
│   └── workflows/
│       └── python.yml              # GitHub Actions — sharded + Slack + PR comments
├── ci/
│   ├── Jenkinsfile                 # Jenkins — lint → API → smoke → regression
│   └── azure-pipelines.yml        # Azure DevOps — multi-browser regression
├── docker/
│   ├── Dockerfile                  # Python 3.12 + Chrome + Firefox
│   └── docker-compose.yml          # Tests + Selenium Grid (hub + nodes)
├── docs/
│   ├── ARCHITECTURE.md             # Layer diagram + how to add pages/tests
│   ├── REPORTING.md                # HTML, Allure, JUnit XML guides
│   ├── ACCESSIBILITY.md            # WCAG 2.1 usage guide
│   └── SLACK-NOTIFICATIONS.md      # Slack setup for GH Actions, Jenkins, Azure
├── req_scripts/
│   └── install_requirements.sh     # Smart install script with venv creation
├── conftest.py                     # All fixtures — driver, pages, api, helpers
├── pytest.ini                      # pytest config + markers
├── config.yaml                     # Framework configuration
├── .env.example                    # Environment variables template
├── requirements.txt                # Core dependencies
├── requirements-dev.txt            # Dev tools — black, flake8, mypy, pre-commit
├── requirements-ci.txt             # CI-specific dependencies
├── setup.cfg                       # flake8 + mypy + isort config
├── BRANCHES.md                     # Python / Java / JavaScript branch guide
├── CONTRIBUTING.md                 # Contributing guide
├── CHANGELOG.md                    # Version history
└── LICENSE                         # MIT
```

---

## 🧪 Test Suites

| File | Tests | Markers | Target |
|---|---|---|---|
| `test_login.py` | 10 | smoke, regression, e2e | the-internet.herokuapp.com |
| `test_home.py` | 7 | smoke, regression, e2e | the-internet.herokuapp.com |
| `test_brand_site.py` | 30 | smoke, regression, e2e | www.skakarh.com |
| `test_login_data_driven.py` | 8 | smoke, regression, e2e | the-internet.herokuapp.com |
| `test_advanced_interactions.py` | 22 | regression, e2e | the-internet.herokuapp.com |
| `test_api.py` | 10 | api | jsonplaceholder.typicode.com |
| `test_visual.py` | 2 | visual | the-internet.herokuapp.com |
| `test_accessibility.py` | 4 | a11y | the-internet.herokuapp.com |
| **Total** | **93** | | |

---

## 🚀 Running Tests

```bash
# ── All tests ────────────────────────────────────────────────────────────────
pytest tests/ --headless -n 2

# ── By marker ────────────────────────────────────────────────────────────────
pytest -m smoke      --headless -n 2    # critical path — run on every commit
pytest -m regression --headless -n 2    # full suite — run on every PR
pytest -m e2e        --headless -n 2    # UI tests only
pytest -m api                           # API tests — no browser needed
pytest -m a11y       --headless         # WCAG 2.1 accessibility tests
pytest -m visual     --headless         # visual regression tests

# ── By browser ───────────────────────────────────────────────────────────────
pytest tests/ --browser=chrome  --headless -n 2   # default
pytest tests/ --browser=firefox --headless -n 2
pytest tests/ --browser=edge    --headless -n 2
pytest tests/ --browser=safari                    # macOS only, no headless

# ── Specific file or test ─────────────────────────────────────────────────────
pytest tests/e2e/test_login.py         --headless -n 2
pytest tests/e2e/test_brand_site.py    --headless -n 2
pytest tests/api/test_api.py
pytest tests/e2e/test_login.py::TestLogin::test_valid_login --headless

# ── With Allure report ────────────────────────────────────────────────────────
pytest tests/ --headless -n 2 --alluredir=allure-results
allure serve allure-results

# ── With JUnit XML (for CI) ───────────────────────────────────────────────────
pytest tests/ --headless -n 2 --junit-xml=reports/results.xml

# ── Verbose output ────────────────────────────────────────────────────────────
pytest tests/ --headless -n 2 -v --tb=short

# ── Stop on first failure ─────────────────────────────────────────────────────
pytest tests/ --headless -n 2 -x

# ── Re-run failed tests ───────────────────────────────────────────────────────
pytest tests/ --headless -n 2 --lf
```

---

## 🏗️ Page Object Model (POM)

### BasePage — fluent interface

Every page object extends `BasePage` which provides smart waits, interactions, assertions and utilities. All methods return `self` for method chaining.

```python
# src/pages/base_page.py
class BasePage:
    def click(self, locator)           # waits for clickability then clicks
    def type(self, locator, text)      # waits for visibility then types
    def find(self, locator)            # waits for visibility then returns element
    def find_all(self, locator)        # waits for presence then returns all elements
    def get_text(self, locator)        # waits and returns element text
    def get_attribute(self, locator, attr)
    def is_visible(self, locator)      # returns bool — no wait
    def is_present(self, locator)      # returns bool — no wait
    def is_enabled(self, locator)      # returns bool — no wait
    def wait_for_url(self, path)       # waits for URL to contain path
    def wait_for_element(self, locator)
    def wait_for_text_in_element(self, locator, text)
    def accept_alert()
    def dismiss_alert()
    def get_alert_text()
    def hover(self, locator)
    def drag_and_drop(self, source, target)
    def select_by_text(self, locator, text)
    def scroll_to(self, locator)
    def take_screenshot(self, name)
    def execute_script(self, script)
    def switch_to_new_window()
    def switch_to_frame(self, locator)
    def upload_file(self, locator, path)
    def open(self, path)               # navigates to base_url + path
```

### Creating a Page Object

```python
# src/pages/my_page.py
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class MyPage(BasePage):
    # Locators as class attributes
    HEADING       = (By.TAG_NAME, "h1")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    INPUT         = (By.ID, "my-input")

    def open(self) -> "MyPage":
        self.open("/my-page")
        return self

    def submit_form(self, text: str) -> "MyPage":
        self.type(self.INPUT, text)
        self.click(self.SUBMIT_BUTTON)
        return self

    def get_heading(self) -> str:
        return self.get_text(self.HEADING)
```

### Using a Page Object in Tests

```python
# tests/e2e/test_my_page.py
import pytest
from src.pages.my_page import MyPage

@pytest.mark.smoke
def test_submit_form(driver):
    page = MyPage(driver)
    page.open().submit_form("QA Pulse by SK")
    assert page.get_heading() == "Success"
```

### PageFixtures — single import for all pages

```python
# Use the pages fixture — no need to import each page separately
def test_full_flow(pages):
    pages.login.login("tomsmith", "SuperSecretPassword!")
    assert pages.secure.is_logged_in()
    pages.brand.open_blog()
    assert pages.brand.get_blog_post_count() > 0
```

---

## 🧩 BaseComponent — Reusable UI Components

Components are self-contained UI elements composed inside Page Objects. Use them for nav bars, modals, tables, flash messages — any element that appears on multiple pages.

```python
# src/components/base_component.py
class BaseComponent:
    def find(self, locator)
    def find_all(self, locator)
    def click(self, locator)
    def get_text(self, locator)
    def get_all_texts(self, locator)
    def is_visible(self, locator, timeout)
```

### Built-in Components

```python
from src.components.components import NavBar, FlashMessage, DataTable

# NavBar
nav = NavBar(driver)
nav.get_links()              # ['Blog', 'Services', 'Products', 'About']
nav.click_link("Blog")
nav.is_logo_visible()        # True/False

# FlashMessage
flash = FlashMessage(driver)
flash.get_text_content()     # "You logged into a secure area!"
flash.is_success()           # True
flash.is_error()             # False

# DataTable
table = DataTable(driver, table_id="table1")
table.get_headers()          # ['Last Name', 'First Name', 'Email', ...]
table.get_row_count()        # 4
table.get_cell(row=1, col=2) # "John"
table.has_column("Email")    # True
```

### Component Composition in Pages

```python
# src/pages/secure_page.py
class SecurePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.flash = FlashMessage(driver)   # composed component

    def get_flash_message(self) -> str:
        return self.flash.get_text_content()

    def is_flash_success(self) -> bool:
        return self.flash.is_success()
```

---

## 🔌 API Testing

```python
# Using ApiClient directly
from src.api.api_client import ApiClient

client   = ApiClient()
response = client.get("/posts/1")
assert response.status_code == 200
assert response.json()["id"] == 1

# Using ApiFixtures — endpoint wrappers
def test_posts_crud(api):
    # GET
    response = api.posts.get_all()
    assert response.status_code == 200

    # POST
    response = api.posts.create({"userId": 1, "title": "Test", "body": "Body"})
    assert response.status_code == 201

    # PUT
    response = api.posts.update(1, {"title": "Updated"})
    assert response.status_code == 200

    # DELETE
    response = api.posts.delete(1)
    assert response.status_code == 200

    # Users
    response = api.users.get_all()
    assert len(response.json()) == 10
```

---

## 🎭 DataFactory — Test Data Generation

```python
from src.utils.data_factory import DataFactory

# Create a realistic user
user = DataFactory.create_user()
print(user.first_name)  # "Alice"
print(user.email)       # "alice.123@example.com"
print(user.password)    # "Qx7!mN2@kP"

# With overrides
user = DataFactory.create_user(first_name="SK", email="sk@qapulse.dev")

# Product
product = DataFactory.create_product()
print(product.name)   # "Streamlined Solutions"
print(product.price)  # 49.99

# Address
address = DataFactory.create_address()
print(address.city)   # "Dubai"

# Utilities
email  = DataFactory.create_email(domain="qapulse.dev")
number = DataFactory.random_number(1, 9999)
price  = DataFactory.random_price(10.0, 999.0)
```

---

## ⏳ WaitHelper — Advanced Waits

```python
from src.helpers.wait_helper import WaitHelper

waiter = WaitHelper(driver, timeout=30)

# Wait for page conditions
waiter.wait_for_page_load()
waiter.wait_for_ajax()
waiter.wait_for_angular()
waiter.wait_for_url_change(original_url)
waiter.wait_for_element_count(locator, count=3)
waiter.wait_for_attribute_value(locator, "class", "active")

# Retry flaky operations
result = WaitHelper.retry(
    lambda: page.get_text(locator),
    retries=3,
    delay=1.0,
)
```

---

## 📸 Visual Regression

```python
from src.helpers.screenshot_helper import ScreenshotHelper

helper = ScreenshotHelper(driver)

# First run — creates baseline in tests/visual/baselines/
passed, diff = helper.compare_with_baseline("login_page")

# Subsequent runs — compares against baseline
passed, diff = helper.compare_with_baseline("login_page", threshold=0.05)
assert passed, f"Visual diff too high: {diff:.2%}"

# Update baseline after intentional UI change
helper.update_baseline("login_page")
```

---

## ♿ Accessibility Testing

```python
from src.helpers.a11y_helper import A11yHelper

a11y = A11yHelper(driver)

# Assert methods
a11y.assert_no_violations()           # fail on any violation
a11y.assert_no_critical_violations()  # fail on critical only
a11y.assert_no_serious_or_critical()  # fail on critical + serious

# Get full results
result = a11y.analyze(context="main")
print(f"Violations: {result.violations_count}")
print(f"Critical:   {result.critical_count}")
for v in result.violations:
    print(f"  [{v.impact.upper()}] {v.id}: {v.help}")
```

---

## 🌐 Cross-Browser Support

```bash
pytest tests/ --browser=chrome  --headless -n 2   # default
pytest tests/ --browser=firefox --headless -n 2
pytest tests/ --browser=edge    --headless -n 2
pytest tests/ --browser=safari                    # macOS only, no headless
```

| Browser | Local | Headless | Remote Grid |
|---|---|---|---|
| Chrome | ✅ | ✅ | ✅ |
| Firefox | ✅ | ✅ | ✅ |
| Edge | ✅ | ✅ | ✅ |
| Safari | ✅ | ❌ | ❌ |

---

## 📊 Reporting

```bash
# HTML Report — generated automatically
pytest tests/ --headless -n 2
open reports/report.html

# Allure Report — rich with history + screenshots
pytest tests/ --headless -n 2 --alluredir=allure-results
allure serve allure-results

# JUnit XML — for CI systems
pytest tests/ --headless -n 2 --junit-xml=reports/results.xml
```

Screenshots are automatically captured on every test failure, saved to `reports/screenshots/`, and attached to Allure reports.

---

## ⚙️ Configuration

```bash
cp .env.example .env
```

```bash
# Target URLs
BASE_URL=https://the-internet.herokuapp.com
API_BASE_URL=https://jsonplaceholder.typicode.com
BRAND_URL=https://www.skakarh.com

# Browser
BROWSER=chrome
HEADLESS=false
WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20
PAGE_LOAD_TIMEOUT=30

# Remote Grid (optional)
REMOTE_URL=
GRID_ENABLED=false

# BrowserStack (optional)
BROWSERSTACK_USERNAME=
BROWSERSTACK_ACCESS_KEY=

# Slack (optional)
SLACK_WEBHOOK_URL=
```

---

## 🏷️ pytest Markers

```bash
pytest -m smoke        # fast, critical path — run on every commit
pytest -m regression   # full suite — run on every PR
pytest -m sanity       # quick sanity after deployment
pytest -m e2e          # UI/browser tests
pytest -m api          # API tests — no browser needed
pytest -m visual       # visual regression
pytest -m a11y         # accessibility
pytest -m critical     # must-never-fail business tests
pytest -m slow         # tests > 30 seconds
```

---

## 🔧 Install Options

```bash
# Core only
bash req_scripts/install_requirements.sh

# Core + dev tools (black, flake8, mypy, pre-commit)
bash req_scripts/install_requirements.sh --dev

# Core + CI extras
bash req_scripts/install_requirements.sh --ci
```

---

## 🐳 Docker

```bash
# Run all tests in Docker
docker-compose -f docker/docker-compose.yml run tests

# Smoke only
docker-compose -f docker/docker-compose.yml run smoke

# API tests only
docker-compose -f docker/docker-compose.yml run api

# Full Selenium Grid (hub + Chrome + Firefox nodes)
docker-compose -f docker/docker-compose.yml up selenium-hub chrome-node firefox-node
docker-compose -f docker/docker-compose.yml run grid-tests
```

---

## 🔁 CI/CD

### GitHub Actions
Triggered on every push and PR to `master`.
- **Lint job** — Black + Flake8
- **API job** — 10 API tests, no browser
- **E2E job** — sharded across 2 runners, parallel execution
- **Slack notifications** — pass/fail alerts
- **PR comments** — test results posted to PR automatically

Add `SLACK_WEBHOOK_URL` to GitHub repo secrets to enable Slack notifications.

### Jenkins
```bash
# Uses ci/Jenkinsfile
# Stages: Checkout → Setup → Lint → API Tests → Smoke → Regression → Accessibility
```

### Azure DevOps
```bash
# Uses ci/azure-pipelines.yml
# Stages: Quality → API → Smoke → Regression (Chrome + Firefox parallel)
```

---

## 🗺️ Roadmap

| Branch | Language | Status |
|---|---|---|
| `master` | Python 3.12 + pytest | ✅ Live — 87 tests |
| `java` | Java 17 + Maven + TestNG | 🔜 Coming Soon |
| `javascript` | TypeScript + WebdriverIO | 🔜 Coming Soon |

---

## 🔗 Related Repositories

| Repo | Description |
|---|---|
| [playwright-boilerplate](https://github.com/QAPulse-by-SK/playwright-boilerplate) | Playwright TypeScript + JavaScript · 101 tests |
| [cypress-boilerplate](https://github.com/QAPulse-by-SK/cypress-boilerplate) | Cypress 13 TypeScript + JavaScript · 48 tests |
| [QAPulseSK-assert](https://github.com/QAPulse-by-SK/QAPulseSK-assert) | Cross-framework assertions — fuzzy match, schema, AI |
| [QAPulseSK-report](https://github.com/QAPulse-by-SK/QAPulseSK-report) | Dark-theme HTML reports + Slack + AI failure analysis |
| [QAPulseSK-gen](https://github.com/QAPulse-by-SK/QAPulseSK-gen) | HAR → Playwright/Cypress tests in 2ms |

---

MIT © [QA Pulse by SK](https://www.skakarh.com)

*Created by QA Pulse by SK · skakarh.com*
