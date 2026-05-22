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
[![QA Pulse by SK](https://img.shields.io/badge/QAPulse--by--SK-skakarh.com-f59e0b?style=flat-square)](https://www.skakarh.com)

<br/>

🌐 **[www.skakarh.com](https://www.skakarh.com)** &nbsp;|&nbsp; 📦 **[Products](https://www.skakarh.com/products/)** &nbsp;|&nbsp; 🏢 **[QAPulse-by-SK](https://github.com/QAPulse-by-SK)**

</div>

---

## 🌿 Branch Strategy

| Branch | Language | Framework | Status |
|---|---|---|---|
| `master` | **Python 3.12+** | pytest + Selenium 4 | ✅ Live |
| `java` | Java 17+ | Maven + TestNG + Allure | 🔜 Coming Soon |
| `javascript` | TypeScript | WebdriverIO + Mocha | 🔜 Coming Soon |

---

## 🐍 Python Branch (master)

### Quick Start

```bash
git clone https://github.com/QAPulse-by-SK/selenium-boilerplate.git
cd selenium-boilerplate
bash req_scripts/install_requirements.sh
cp .env.example .env
pytest tests/ --headless -n 2
```

### Requirements

- Python 3.12+
- Chrome / Firefox / Edge / Safari
- No manual driver download — Selenium 4 manages it automatically

---

## 📁 Project Structure

```
selenium-boilerplate/
├── src/
│   ├── pages/              # Page Object Model
│   │   ├── base_page.py    # BasePage — fluent interface, smart waits
│   │   ├── login_page.py   # LoginPage
│   │   ├── home_page.py    # HomePage
│   │   └── brand_site_page.py  # skakarh.com page object
│   ├── api/
│   │   └── api_client.py   # requests-based HTTP client
│   ├── helpers/
│   │   ├── driver_factory.py   # Chrome/Firefox/Edge/Safari factory
│   │   ├── wait_helper.py      # Advanced waits + retry decorator
│   │   ├── screenshot_helper.py # Visual regression with Pillow
│   │   └── a11y_helper.py      # WCAG 2.1 via axe-selenium-python
│   ├── utils/
│   │   ├── logger.py       # Colour-coded logger with timestamps
│   │   ├── config_reader.py # config.yaml + .env support
│   │   └── data_factory.py  # Faker-based test data generation
│   └── constants/
│       └── constants.py    # URLs, credentials, markers, timeouts
├── tests/
│   ├── e2e/
│   │   ├── test_login.py                  # 10 tests — login flows
│   │   ├── test_home.py                   # 7 tests  — homepage
│   │   ├── test_brand_site.py             # 30 tests — skakarh.com E2E
│   │   ├── test_login_data_driven.py      # 8 tests  — JSON + parametrize
│   │   └── test_advanced_interactions.py  # 22 tests — checkboxes, dropdowns, alerts, drag&drop, windows, hovers, tables
│   ├── api/
│   │   └── test_api.py     # 10 tests — CRUD + schema validation
│   ├── visual/
│   │   └── test_visual.py  # Visual regression tests
│   └── accessibility/
│       └── test_accessibility.py  # WCAG 2.1 tests
├── test-data/
│   └── users.json          # Data-driven test fixtures
├── req_scripts/
│   └── install_requirements.sh  # Smart install script
├── conftest.py             # Fixtures — driver, pages, helpers
├── pytest.ini              # pytest config + markers
├── config.yaml             # Framework configuration
├── .env.example            # Environment variables template
├── requirements.txt        # Core dependencies
├── requirements-dev.txt    # Dev tools (black, flake8, mypy)
└── requirements-ci.txt     # CI dependencies
```

---

## 🧪 Test Suites

| File | Tests | Markers | Target |
|---|---|---|---|
| `test_login.py` | 10 | smoke, regression | the-internet.herokuapp.com |
| `test_home.py` | 7 | smoke, regression | the-internet.herokuapp.com |
| `test_brand_site.py` | 30 | smoke, regression | www.skakarh.com |
| `test_login_data_driven.py` | 8 | smoke, regression | the-internet.herokuapp.com |
| `test_advanced_interactions.py` | 22 | regression | the-internet.herokuapp.com |
| `test_api.py` | 10 | api | jsonplaceholder.typicode.com |
| **Total** | **87** | | |

---

## 🚀 Running Tests

```bash
# All tests (parallel — 4x faster)
pytest tests/ --headless -n 2

# By marker
pytest -m smoke --headless -n 2
pytest -m regression --headless -n 2
pytest -m api
pytest -m e2e --headless -n 2
pytest -m a11y --headless
pytest -m visual --headless

# Specific browser
pytest tests/ --browser=firefox --headless -n 2
pytest tests/ --browser=edge    --headless -n 2
pytest tests/ --browser=safari               # Safari doesn't support headless

# Specific file
pytest tests/e2e/test_login.py --headless -n 2
pytest tests/api/test_api.py

# With Allure report
pytest tests/ --headless -n 2 --alluredir=allure-results
allure serve allure-results
```

---

## 🏗️ Framework Features

### Page Object Model
```python
# Fluent interface — chain methods
login_page.open_login_page() \
          .enter_username("tomsmith") \
          .enter_password("SuperSecretPassword!") \
          .click_login()
```

### Smart Waits — BasePage
```python
# Built-in explicit waits on every interaction
page.click(locator)          # waits for clickability
page.find(locator)           # waits for visibility
page.wait_for_url("/secure") # waits for URL change
page.wait_for_text(locator, "Hello World!")
```

### Data-Driven Tests
```python
# JSON fixture — test-data/users.json
@pytest.mark.parametrize("user", load_users())
def test_login_data_driven(driver, user):
    page = LoginPage(driver)
    page.login(user["username"], user["password"])
    assert page.is_login_successful() == (user["expected"] == "success")
```

### DataFactory — Faker
```python
user    = DataFactory.create_user()
product = DataFactory.create_product()
address = DataFactory.create_address()
email   = DataFactory.create_email(domain="qapulse.dev")
```

### API Testing
```python
client   = ApiClient()
response = client.get("/posts/1")
assert response.status_code == 200
assert isinstance(response.json()["id"], int)
```

### Visual Regression
```python
# First run — creates baseline
screenshot_helper.compare_with_baseline("login_page")

# Subsequent runs — compares against baseline
passed, diff = screenshot_helper.compare_with_baseline("login_page")
assert passed, f"Visual diff: {diff:.2%}"
```

### Accessibility Testing
```python
a11y = A11yHelper(driver)
a11y.assert_no_critical_violations()
a11y.assert_no_serious_or_critical()
result = a11y.analyze()
print(f"Violations: {result.violations_count}")
```

### WaitHelper — Advanced Waits
```python
waiter = WaitHelper(driver)
waiter.wait_for_page_load()
waiter.wait_for_ajax()
waiter.wait_for_url_change(original_url)
result = WaitHelper.retry(lambda: page.get_text(locator), retries=3)
```

### Auto Screenshot on Failure
Every failed test automatically captures a screenshot saved to `reports/screenshots/` and attached to the Allure report.

---

## 🌐 Cross-Browser Support

| Browser | Local | Headless | Remote Grid | Notes |
|---|---|---|---|---|
| Chrome | ✅ | ✅ | ✅ | Default |
| Firefox | ✅ | ✅ | ✅ | |
| Edge | ✅ | ✅ | ✅ | |
| Safari | ✅ | ❌ | ❌ | macOS only |

---

## 📊 Reporting

### HTML Report (default)
```bash
pytest tests/ --headless -n 2
open reports/report.html
```

### Allure Report
```bash
pytest tests/ --headless -n 2 --alluredir=allure-results
allure serve allure-results
```

---

## ⚙️ Configuration

### .env file
```bash
cp .env.example .env
```

Key settings:
```bash
BASE_URL=https://the-internet.herokuapp.com
BROWSER=chrome
HEADLESS=false
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20
PAGE_LOAD_TIMEOUT=30
```

### Pytest markers
```bash
pytest -m smoke      # fast, critical path — run on every commit
pytest -m regression # full suite — run on every PR
pytest -m e2e        # UI tests only
pytest -m api        # API tests only (no browser)
pytest -m a11y       # accessibility tests
pytest -m visual     # visual regression tests
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
| [playwright-boilerplate](https://github.com/QAPulse-by-SK/playwright-boilerplate) | Playwright TypeScript + JavaScript |
| [cypress-boilerplate](https://github.com/QAPulse-by-SK/cypress-boilerplate) | Cypress 13 TypeScript + JavaScript |
| [QAPulseSK-assert](https://github.com/QAPulse-by-SK/QAPulseSK-assert) | Cross-framework assertions |
| [QAPulseSK-report](https://github.com/QAPulse-by-SK/QAPulseSK-report) | Dark-theme HTML reports |
| [QAPulseSK-gen](https://github.com/QAPulse-by-SK/QAPulseSK-gen) | HAR → tests in 2ms |

---

MIT © [QA Pulse by SK](https://www.skakarh.com)

*Created by QA Pulse by SK · skakarh.com*
