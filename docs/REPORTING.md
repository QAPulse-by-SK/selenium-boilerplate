# Reporting Guide
**QA Pulse by SK — Selenium Python Boilerplate**
🌐 www.skakarh.com

---

## HTML Report (default — zero config)

Generated automatically after every run at `reports/report.html`.

```bash
pytest tests/ --headless -n 2
open reports/report.html
```

---

## Allure Report (rich — with history + screenshots)

```bash
# Install Allure CLI (macOS)
brew install allure

# Run with Allure
pytest tests/ --headless -n 2 --alluredir=allure-results

# View report
allure serve allure-results

# Generate static HTML
allure generate allure-results --clean -o allure-report
open allure-report/index.html
```

---

## JUnit XML (for CI systems)

```bash
pytest tests/ --junit-xml=reports/results.xml
```

Jenkins, Azure DevOps, and GitHub Actions all consume JUnit XML natively.

---

## Screenshots on Failure

Every failed test automatically captures a screenshot to `reports/screenshots/`.

Screenshots are also attached to the Allure report automatically via the `pytest_runtest_makereport` hook in `conftest.py`.

---

## Running by Marker

```bash
pytest -m smoke      --html=reports/smoke.html      --self-contained-html
pytest -m regression --html=reports/regression.html --self-contained-html
pytest -m api        --html=reports/api.html         --self-contained-html
```
