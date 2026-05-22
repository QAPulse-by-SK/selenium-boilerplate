# Architecture Guide
**QA Pulse by SK — Selenium Python Boilerplate**
🌐 www.skakarh.com

---

## Core Design Principles

1. **Single Responsibility** — each class does one thing well
2. **DRY** — no copy-paste; shared logic lives in helpers/base classes
3. **Explicit over Magic** — no hidden globals, all dependencies injected via fixtures
4. **Fail Fast** — assertions close to actions; no `time.sleep()`
5. **Self-Documenting** — tests read like plain English sentences

---

## Layer Architecture

```
┌─────────────────────────────────────────────────┐
│           TEST FILES (tests/)                    │
│  e2e/ | api/ | visual/ | accessibility/         │
└──────────────────┬──────────────────────────────┘
                   │ use fixtures from
┌──────────────────▼──────────────────────────────┐
│           CONFTEST (conftest.py)                 │
│   driver | login_page | api_client | a11y_helper │
└──────┬─────────────────────┬────────────────────┘
       │                     │
┌──────▼──────┐     ┌────────▼────────┐
│ PAGE OBJECTS│     │   API CLIENT    │
│ src/pages/  │     │   src/api/      │
│ BasePage    │     │   ApiClient     │
│ LoginPage   │     └─────────────────┘
│ HomePage    │
│ BrandSitePage│
└──────┬──────┘
       │ uses
┌──────▼──────────────────────────────────────────┐
│          HELPERS & UTILITIES                     │
│  DriverFactory | WaitHelper | ScreenshotHelper  │
│  A11yHelper | DataFactory | Logger              │
└──────┬──────────────────────────────────────────┘
       │ reads
┌──────▼──────────────────────────────────────────┐
│          CONFIG & CONSTANTS                      │
│  config.yaml | .env | constants.py              │
└─────────────────────────────────────────────────┘
```

---

## Adding a New Page

1. Create `src/pages/my_page.py` extending `BasePage`
2. Add locators as class attributes
3. Add fixture in `conftest.py`
4. Write tests in `tests/e2e/test_my_page.py`

```python
# src/pages/my_page.py
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class MyPage(BasePage):
    HEADING = (By.TAG_NAME, "h1")

    def open(self) -> "MyPage":
        self.open("/my-page")
        return self

    def get_heading(self) -> str:
        return self.get_text(self.HEADING)
```

## Adding a New Test

```python
# tests/e2e/test_my_page.py
import pytest
from src.pages.my_page import MyPage

@pytest.mark.smoke
def test_my_page_loads(driver):
    page = MyPage(driver)
    page.open()
    assert page.get_heading() != ""
```

## Adding API Tests

```python
# tests/api/test_my_api.py
import pytest
from src.api.api_client import ApiClient

@pytest.mark.api
def test_get_item(api_client: ApiClient):
    response = api_client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
```
