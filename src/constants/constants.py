"""
QA Pulse by SK — Selenium Boilerplate
Constants — URLs, credentials, test tags.
"""

# ── URLs ──────────────────────────────────────────────────────────────────────
class URLs:
    BASE          = "https://the-internet.herokuapp.com"
    LOGIN         = "/login"
    CHECKBOXES    = "/checkboxes"
    DROPDOWN      = "/dropdown"
    DYNAMIC_LOAD  = "/dynamic_loading/1"
    ALERTS        = "/javascript_alerts"
    DRAG_DROP     = "/drag_and_drop"
    UPLOAD        = "/upload"
    FRAMES        = "/frames"
    WINDOWS       = "/windows"
    TABLES        = "/tables"
    HOVERS        = "/hovers"
    INFINITE_SCROLL = "/infinite_scroll"


# ── Credentials ───────────────────────────────────────────────────────────────
class Credentials:
    VALID_USERNAME   = "tomsmith"
    VALID_PASSWORD   = "SuperSecretPassword!"
    INVALID_USERNAME = "wronguser"
    INVALID_PASSWORD = "wrongpassword"


# ── Test Markers ──────────────────────────────────────────────────────────────
class Tags:
    SMOKE       = "smoke"
    REGRESSION  = "regression"
    SANITY      = "sanity"
    CRITICAL    = "critical"
    E2E         = "e2e"
    API         = "api"
    VISUAL      = "visual"
    A11Y        = "a11y"
    SLOW        = "slow"
    FLAKY       = "flaky"


# ── Timeouts ─────────────────────────────────────────────────────────────────
class Timeouts:
    SHORT    = 5
    DEFAULT  = 10
    LONG     = 20
    VERY_LONG = 30


# ── Browsers ──────────────────────────────────────────────────────────────────
class Browsers:
    CHROME  = "chrome"
    FIREFOX = "firefox"
    EDGE    = "edge"
    SAFARI  = "safari"
