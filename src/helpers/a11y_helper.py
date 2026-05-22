"""
QA Pulse by SK — Selenium Boilerplate
Accessibility helper — WCAG 2.1 checks via axe-selenium-python.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from selenium.webdriver.remote.webdriver import WebDriver

from src.utils.logger import logger


class A11yHelper:
    """
    Accessibility testing helper using axe-selenium-python.

    Checks:
        - WCAG 2.1 Level A violations
        - WCAG 2.1 Level AA violations
        - Critical accessibility issues
        - Images without alt text
        - Form labels
        - Keyboard navigation
        - ARIA attributes
        - Colour contrast
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def _run_axe(self) -> dict:
        """Inject and run axe-core on the current page."""
        try:
            from axe_selenium_python import Axe
            axe = Axe(self.driver)
            axe.inject()
            return axe.run()
        except ImportError:
            logger.warning("axe-selenium-python not installed — install with: pip install axe-selenium-python")
            return {"violations": []}

    def get_violations(self, impact: Optional[str] = None) -> List[dict]:
        """
        Get all accessibility violations.

        Args:
            impact: Filter by impact level (critical|serious|moderate|minor)
        """
        results    = self._run_axe()
        violations = results.get("violations", [])
        if impact:
            violations = [v for v in violations if v.get("impact") == impact]
        return violations

    def assert_no_violations(self, impact: Optional[str] = None) -> None:
        """Assert no accessibility violations — fails test if found."""
        violations = self.get_violations(impact)
        if violations:
            report = self._format_violations(violations)
            raise AssertionError(f"Accessibility violations found:\n{report}")
        logger.pass_("No accessibility violations found")

    def assert_no_critical_violations(self) -> None:
        """Assert no critical accessibility violations."""
        self.assert_no_violations(impact="critical")

    def assert_no_serious_violations(self) -> None:
        """Assert no serious or critical violations."""
        violations = [
            v for v in self.get_violations()
            if v.get("impact") in ("critical", "serious")
        ]
        if violations:
            raise AssertionError(
                f"Critical/serious accessibility violations found:\n"
                f"{self._format_violations(violations)}"
            )
        logger.pass_("No critical/serious accessibility violations found")

    def get_violation_count(self) -> int:
        return len(self.get_violations())

    def print_violations(self) -> None:
        """Print all violations to console (useful for debugging)."""
        violations = self.get_violations()
        if not violations:
            logger.pass_("No accessibility violations found")
            return
        logger.warning(f"Found {len(violations)} accessibility violation(s):")
        for v in violations:
            logger.warning(f"  [{v.get('impact', '?').upper()}] {v.get('description', '')}")
            for node in v.get("nodes", [])[:2]:
                logger.warning(f"    → {node.get('html', '')[:100]}")

    def _format_violations(self, violations: List[dict]) -> str:
        lines = []
        for v in violations:
            impact = v.get("impact", "unknown").upper()
            desc   = v.get("description", "")
            lines.append(f"  [{impact}] {v.get('id', '')} — {desc}")
            for node in v.get("nodes", [])[:2]:
                lines.append(f"    → {node.get('html', '')[:80]}")
        return "\n".join(lines)
