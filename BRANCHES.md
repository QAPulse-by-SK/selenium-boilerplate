# Branch Guide
**QA Pulse by SK — Selenium Boilerplate** · www.skakarh.com

---

## Branch Strategy

| Branch | Language | Framework | Status |
|---|---|---|---|
| `master` | Python 3.12+ | pytest + Selenium 4 | ✅ Live |
| `java` | Java 17+ | Maven + TestNG + Allure | 🔜 Coming Soon |
| `javascript` | TypeScript | WebdriverIO + Mocha | 🔜 Coming Soon |

All branches are **feature-identical** — same test coverage, same CI/CD pipelines, same folder structure. Choose the language your team works in.

---

## Python (master)

```bash
git clone https://github.com/QAPulse-by-SK/selenium-boilerplate.git
cd selenium-boilerplate
bash req_scripts/install_requirements.sh
cp .env.example .env
pytest tests/ --headless -n 2
```

**Key files:**
- `conftest.py` — pytest fixtures
- `pytest.ini` — markers + configuration
- `src/pages/base_page.py` — fluent BasePage
- `src/helpers/driver_factory.py` — Chrome/Firefox/Edge/Safari

---

## Java (java branch)

```bash
git clone -b java https://github.com/QAPulse-by-SK/selenium-boilerplate.git
cd selenium-boilerplate
mvn clean test
```

**Stack:** Java 17 · Maven · TestNG · Allure · WebDriverManager · ExtentReports

---

## JavaScript (javascript branch)

```bash
git clone -b javascript https://github.com/QAPulse-by-SK/selenium-boilerplate.git
cd selenium-boilerplate
npm install
npx wdio run wdio.conf.ts
```

**Stack:** TypeScript · WebdriverIO 8 · Mocha · Allure · Chai

---

*Created by QA Pulse by SK · skakarh.com*
