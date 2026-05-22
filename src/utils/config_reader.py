"""
QA Pulse by SK — Selenium Boilerplate
ConfigReader — reads config.yaml and .env files
Wraps the module-level config functions for class-based usage.
"""
from __future__ import annotations

import os
from typing import Any

import yaml
from dotenv import load_dotenv

load_dotenv()


def _load_yaml() -> dict:
    if os.path.exists("config.yaml"):
        with open("config.yaml") as f:
            return yaml.safe_load(f) or {}
    return {}


_CONFIG = _load_yaml()


def get(key: str, default: Any = None) -> Any:
    """Get config value — env vars override config.yaml."""
    env_val = os.getenv(key.upper())
    if env_val is not None:
        if str(env_val).lower() in ("true", "false"):
            return str(env_val).lower() == "true"
        if str(env_val).isdigit():
            return int(env_val)
        return env_val
    parts = key.split(".")
    val   = _CONFIG
    for part in parts:
        if isinstance(val, dict):
            val = val.get(part)
        else:
            return default
    return val if val is not None else default


class ConfigReader:
    """Class-based wrapper for config access."""

    def get(self, key: str, default: Any = None) -> Any:
        return get(key, default)


# ── Convenience accessors ─────────────────────────────────────────────────────
BASE_URL          = get("BASE_URL",           "https://the-internet.herokuapp.com")
BRAND_URL         = get("BRAND_URL",          "https://www.skakarh.com")
API_BASE_URL      = get("API_BASE_URL",       "https://jsonplaceholder.typicode.com")
BROWSER           = str(get("BROWSER",        "chrome")).lower()
HEADLESS          = get("HEADLESS",           False)
IMPLICIT_WAIT     = int(get("IMPLICIT_WAIT",  10))
EXPLICIT_WAIT     = int(get("EXPLICIT_WAIT",  20))
PAGE_LOAD_TIMEOUT = int(get("PAGE_LOAD_TIMEOUT", 30))
SCREENSHOT_DIR    = get("SCREENSHOT_DIR",     "reports/screenshots")
TEST_USERNAME     = get("TEST_USERNAME",      "tomsmith")
TEST_PASSWORD     = get("TEST_PASSWORD",      "SuperSecretPassword!")
REMOTE_URL        = get("REMOTE_URL",         "")
SLACK_WEBHOOK     = get("SLACK_WEBHOOK_URL",  "")
ENVIRONMENT       = str(get("ENVIRONMENT",    "local")).lower()
