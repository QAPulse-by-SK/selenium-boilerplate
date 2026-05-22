# Accessibility Testing Guide
**QA Pulse by SK — Selenium Python Boilerplate** · www.skakarh.com

---

## Overview

Built on `axe-selenium-python` — the Python binding for axe-core, the industry standard for automated WCAG 2.1 testing.

---

## Usage

```python
from src.helpers.a11y_helper import A11yHelper

def test_no_critical_violations(driver):
    page = BasePage(driver)
    page.open("/login")

    a11y = A11yHelper(driver)

    # Fail only on critical violations
    a11y.assert_no_critical_violations()

    # Fail on critical + serious violations
    a11y.assert_no_serious_or_critical()

    # Fail on any violation
    a11y.assert_no_violations()

    # Get full results for reporting
    result = a11y.analyze()
    print(f"Total violations : {result.violations_count}")
    print(f"Critical         : {result.critical_count}")
    print(f"Serious          : {result.serious_count}")
    for v in result.violations:
        print(f"  [{v.impact.upper()}] {v.id}: {v.help}")
        print(f"  Help URL: {v.help_url}")
```

---

## Scoped Analysis

```python
# Analyse only a section of the page
result = a11y.analyze(context="main")
result = a11y.analyze(context="#login-form")
result = a11y.analyze(context=".service-card")
```

---

## Running

```bash
# All accessibility tests
pytest tests/accessibility/ --headless -v

# Via marker
pytest -m a11y --headless -v

# With Allure
pytest -m a11y --headless --alluredir=allure-results
allure serve allure-results
```

---

## WCAG 2.1 Levels

| Impact | Level | Should fail? |
|---|---|---|
| Critical | WCAG 2.1 AA | ✅ Always |
| Serious | WCAG 2.1 AA | ✅ Recommended |
| Moderate | WCAG 2.1 AA | ⚠️ Optional |
| Minor | WCAG 2.1 AAA | ⚠️ Optional |

---

*Created by QA Pulse by SK · skakarh.com*
