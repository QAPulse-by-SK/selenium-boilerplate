"""
QA Pulse by SK — Selenium Boilerplate
src/types/types.py — Shared type definitions (dataclasses)

Python equivalent of TypeScript interfaces.
Used across pages, helpers, and tests for type safety.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Literal, Optional


# ─── User ────────────────────────────────────────────────────────────────────

@dataclass
class User:
    username: str
    password: str


@dataclass
class UserProfile:
    id:    int
    name:  str
    email: str
    role:  Literal["admin", "user", "guest"] = "user"


# ─── API ─────────────────────────────────────────────────────────────────────

@dataclass
class ApiResponse:
    status:  int
    body:    Any
    headers: Dict[str, str] = field(default_factory=dict)
    elapsed: float = 0.0

    @property
    def ok(self) -> bool:
        return self.status < 400


@dataclass
class Post:
    userId: int
    title:  str
    body:   str
    id:     Optional[int] = None


@dataclass
class Comment:
    postId: int
    name:   str
    email:  str
    body:   str
    id:     Optional[int] = None


# ─── Test Config ─────────────────────────────────────────────────────────────

@dataclass
class TestEnvironment:
    base_url:     str
    brand_url:    str
    api_base_url: str
    credentials:  User


# ─── Visual Regression ───────────────────────────────────────────────────────

@dataclass
class SnapshotOptions:
    full_page:            bool  = True
    max_diff_pixel_ratio: float = 0.1
    threshold:            float = 0.1


# ─── Accessibility ───────────────────────────────────────────────────────────

ImpactLevel = Literal["critical", "serious", "moderate", "minor"]


@dataclass
class A11yViolation:
    id:          str
    impact:      str
    description: str
    help:        str
    help_url:    str
    nodes_count: int


@dataclass
class A11yResult:
    passed:           bool
    violations:       List[A11yViolation]
    violations_count: int
    critical_count:   int
    serious_count:    int
    moderate_count:   int
    minor_count:      int


# ─── Browser ─────────────────────────────────────────────────────────────────

BrowserName = Literal["chrome", "firefox", "edge", "safari"]


@dataclass
class BrowserConfig:
    name:              BrowserName = "chrome"
    headless:          bool        = False
    window_width:      int         = 1280
    window_height:     int         = 720
    implicit_wait:     int         = 10
    explicit_wait:     int         = 20
    page_load_timeout: int         = 30
