# Contributing Guide
**QA Pulse by SK — Selenium Boilerplate** · www.skakarh.com

---

## Setup

```bash
git clone https://github.com/QAPulse-by-SK/selenium-boilerplate.git
cd selenium-boilerplate
bash req_scripts/install_requirements.sh --dev
cp .env.example .env
pre-commit install
```

---

## Branch Targets

| Change type | Target branch |
|---|---|
| Python fixes/features | `master` |
| Java fixes/features | `java` |
| JavaScript fixes/features | `javascript` |

---

## Code Standards

```bash
# Format
black src/ tests/

# Lint
flake8 src/ tests/ --max-line-length=120

# Type check
mypy src/

# Run all tests before PR
pytest tests/ --headless -n 2
```

---

## Adding Tests

- Place E2E tests in `tests/e2e/test_*.py`
- Place API tests in `tests/api/test_*.py`
- Use appropriate markers: `@pytest.mark.smoke`, `@pytest.mark.regression`
- Every test must have a docstring

---

PRs reviewed within 48 hours · MIT License
