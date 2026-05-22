"""
QA Pulse by SK — Selenium Boilerplate
Colour-coded logger with timestamps.
"""

import logging
import sys
from datetime import datetime


class QAPulseLogger:
    """Colour-coded terminal logger with timestamps."""

    COLOURS = {
        "DEBUG":    "\033[36m",
        "INFO":     "\033[32m",
        "WARNING":  "\033[33m",
        "ERROR":    "\033[31m",
        "CRITICAL": "\033[35m",
        "RESET":    "\033[0m",
        "BOLD":     "\033[1m",
        "DIM":      "\033[2m",
    }

    class ColouredFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:
            colours = QAPulseLogger.COLOURS
            level   = record.levelname
            colour  = colours.get(level, colours["RESET"])
            reset   = colours["RESET"]
            dim     = colours["DIM"]
            bold    = colours["BOLD"]
            ts      = datetime.now().strftime("%H:%M:%S")
            prefix  = f"{dim}[{ts}]{reset} {bold}{colour}[{level[:4]}]{reset}"
            message = f"{colour}{record.getMessage()}{reset}"
            return f"🎭 [QA Pulse] {prefix} {message}"

    def __init__(self, name: str = "qapulse") -> None:
        self._logger = logging.getLogger(name)
        if not self._logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(self.ColouredFormatter())
            self._logger.addHandler(handler)
            self._logger.setLevel(logging.DEBUG)
            self._logger.propagate = False

    def debug(self, msg: str)    -> None: self._logger.debug(msg)
    def info(self, msg: str)     -> None: self._logger.info(msg)
    def warning(self, msg: str)  -> None: self._logger.warning(msg)
    def error(self, msg: str)    -> None: self._logger.error(msg)
    def critical(self, msg: str) -> None: self._logger.critical(msg)

    def step(self, msg: str) -> None:
        self._logger.info(f"→ {msg}")

    def pass_(self, msg: str) -> None:
        self._logger.info(f"✅ {msg}")

    def fail(self, msg: str) -> None:
        self._logger.error(f"❌ {msg}")


# Singleton instance
logger = QAPulseLogger()

# Alias — allows both Logger(__name__) and logger usage patterns
Logger = QAPulseLogger
