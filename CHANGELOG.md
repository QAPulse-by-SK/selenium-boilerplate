# Changelog
**QA Pulse by SK — Selenium Boilerplate** · www.skakarh.com

---

## [1.0.0] — 2025-05-22

### Added — Python (master branch)

**Tests — 87 passing**
- `test_login.py` — 10 tests: valid/invalid login, logout, field masking, URL
- `test_home.py` — 7 tests: heading, nav links, navigation flows
- `test_brand_site.py` — 30 tests: skakarh.com homepage, blog, services, products, about
- `test_login_data_driven.py` — 8 tests: JSON fixtures + pytest parametrize
- `test_advanced_interactions.py` — 22 tests: checkboxes, dropdowns, dynamic loading, alerts, drag & drop, windows, hovers, tables
- `test_api.py` — 10 tests: CRUD, schema validation, response time

**Framework**
- Page Object Model — BasePage with fluent interface + smart waits
- DriverFactory — Chrome, Firefox, Edge, Safari (Selenium 4 built-in manager)
- WaitHelper — advanced waits, AJAX wait, Angular wait, retry decorator
- ScreenshotHelper — visual regression with Pillow baseline comparison
- A11yHelper — WCAG 2.1 via axe-selenium-python
- DataFactory — Faker-based test data (UserData, ProductData, AddressData)
- ConfigReader — config.yaml + .env with dot-notation access
- ApiClient — requests-based HTTP client with session management
- Auto screenshot on failure — saved to `reports/screenshots/` + Allure

**CI/CD**
- GitHub Actions — sharded E2E + API jobs + Slack notifications + PR comments
- Jenkinsfile — multi-stage: lint → API → smoke → regression → accessibility
- azure-pipelines.yml — quality checks → API → smoke → multi-browser regression

**Docker**
- Dockerfile — Python 3.12 slim + Chrome + Firefox
- docker-compose.yml — tests, smoke, API, Selenium Grid (hub + Chrome/Firefox nodes)

**Docs**
- ARCHITECTURE.md — layer diagram + how to add pages/tests
- REPORTING.md — HTML, Allure, JUnit XML guides
- ACCESSIBILITY.md — WCAG 2.1 usage guide
- SLACK-NOTIFICATIONS.md — GitHub Actions, Jenkins, Azure DevOps setup
- BRANCHES.md — Python/Java/JavaScript branch guide
