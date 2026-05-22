"""
QA Pulse by SK — Selenium Boilerplate
Screenshot helper — capture, compare, manage baselines.
"""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

from PIL import Image, ImageChops
from selenium.webdriver.remote.webdriver import WebDriver

from src.utils.config_reader import SCREENSHOT_DIR
from src.utils.logger import logger

BASELINE_DIR = "reports/baselines"
DIFF_DIR     = "reports/diffs"


class ScreenshotHelper:
    """Screenshot capture and visual comparison helper."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        os.makedirs(BASELINE_DIR,   exist_ok=True)
        os.makedirs(DIFF_DIR,       exist_ok=True)

    def capture(self, name: str) -> str:
        """Capture a screenshot and return its path."""
        ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{ts}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        self.driver.save_screenshot(filepath)
        logger.info(f"📸 Screenshot: {filepath}")
        return filepath

    def capture_element(self, element, name: str) -> str:
        """Capture screenshot of a specific element."""
        ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{ts}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        element.screenshot(filepath)
        return filepath

    def save_baseline(self, name: str) -> str:
        """Capture and save as baseline for visual regression."""
        filepath = os.path.join(BASELINE_DIR, f"{name}.png")
        self.driver.save_screenshot(filepath)
        logger.info(f"📐 Baseline saved: {filepath}")
        return filepath

    def compare_with_baseline(
        self,
        name: str,
        threshold: float = 0.01
    ) -> Tuple[bool, float]:
        """
        Compare current screenshot with baseline.

        Args:
            name:       Test name (must match baseline filename)
            threshold:  Max allowed difference ratio (0.0 - 1.0)

        Returns:
            Tuple of (passed, diff_ratio)
        """
        baseline_path = os.path.join(BASELINE_DIR, f"{name}.png")
        if not os.path.exists(baseline_path):
            logger.warning(f"No baseline found for '{name}' — saving as baseline")
            self.save_baseline(name)
            return True, 0.0

        # Capture current
        current_path = self.capture(f"{name}_current")

        # Compare
        baseline = Image.open(baseline_path).convert("RGB")
        current  = Image.open(current_path).convert("RGB")

        # Resize if dimensions differ
        if baseline.size != current.size:
            current = current.resize(baseline.size, Image.LANCZOS)

        diff       = ImageChops.difference(baseline, current)
        diff_array = list(diff.getdata())
        total_px   = len(diff_array)
        diff_px    = sum(1 for px in diff_array if any(c > 10 for c in px))
        diff_ratio = diff_px / total_px

        passed = diff_ratio <= threshold

        if not passed:
            # Save diff image
            diff_path = os.path.join(DIFF_DIR, f"{name}_diff.png")
            diff.save(diff_path)
            logger.error(
                f"Visual mismatch: {name} — diff ratio: {diff_ratio:.4f} "
                f"(threshold: {threshold}) — diff saved: {diff_path}"
            )
        else:
            logger.pass_(f"Visual match: {name} — diff ratio: {diff_ratio:.4f}")

        return passed, diff_ratio
