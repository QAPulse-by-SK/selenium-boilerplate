#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# QA Pulse by SK — Selenium Boilerplate
# Install script — handles venv creation and dependency installation
#
# Usage:
#   bash req_scripts/install_requirements.sh          # core only
#   bash req_scripts/install_requirements.sh --dev    # core + dev tools
#   bash req_scripts/install_requirements.sh --ci     # core + CI extras
# ─────────────────────────────────────────────────────────────────────────────

set -e

PYTHON="python3"
VENV_DIR=".venv"
MODE=${1:-""}

echo ""
echo "🎭 QA Pulse by SK — Selenium Boilerplate"
echo "   Python Selenium Test Automation Framework"
echo ""

# ── Check Python version ──────────────────────────────────────────────────────
PYTHON_VERSION=$($PYTHON --version 2>&1 | cut -d' ' -f2)
REQUIRED_MAJOR=3
REQUIRED_MINOR=10

MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)

if [ "$MAJOR" -lt "$REQUIRED_MAJOR" ] || ([ "$MAJOR" -eq "$REQUIRED_MAJOR" ] && [ "$MINOR" -lt "$REQUIRED_MINOR" ]); then
  echo "❌ Python $REQUIRED_MAJOR.$REQUIRED_MINOR+ required. Found: $PYTHON_VERSION"
  exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# ── Create virtualenv if not exists ──────────────────────────────────────────
if [ ! -d "$VENV_DIR" ]; then
  echo "📦 Creating virtual environment at $VENV_DIR..."
  $PYTHON -m venv $VENV_DIR
  echo "✅ Virtual environment created"
else
  echo "✅ Virtual environment already exists at $VENV_DIR"
fi

# ── Activate venv ────────────────────────────────────────────────────────────
source $VENV_DIR/bin/activate
echo "✅ Virtual environment activated"

# ── Upgrade pip ──────────────────────────────────────────────────────────────
pip install --upgrade pip --quiet
echo "✅ pip upgraded"

# ── Install dependencies ─────────────────────────────────────────────────────
if [ "$MODE" = "--dev" ]; then
  echo ""
  echo "📦 Installing core + dev dependencies..."
  pip install -r requirements-dev.txt
  echo ""
  echo "✅ Setting up pre-commit hooks..."
  pre-commit install
elif [ "$MODE" = "--ci" ]; then
  echo ""
  echo "📦 Installing core + CI dependencies..."
  pip install -r requirements-ci.txt
else
  echo ""
  echo "📦 Installing core dependencies..."
  pip install -r requirements.txt
fi

# ── Copy .env.example to .env if not exists ───────────────────────────────────
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  cp .env.example .env
  echo "✅ .env created from .env.example"
fi

echo ""
echo "✅ All dependencies installed successfully!"
echo ""
echo "┌─────────────────────────────────────────────────────┐"
echo "│  Next steps:                                        │"
echo "│                                                     │"
echo "│  1. Activate venv:  source .venv/bin/activate       │"
echo "│  2. Copy env:       cp .env.example .env            │"
echo "│  3. Run tests:      pytest tests/ -v                │"
echo "│  4. Run smoke:      pytest -m smoke -v              │"
echo "│  5. Run parallel:   pytest tests/ -n auto           │"
echo "│  6. Allure report:  pytest --alluredir=allure-results│"
echo "│                     allure serve allure-results     │"
echo "│                                                     │"
echo "└─────────────────────────────────────────────────────┘"
echo ""
echo "  Built by QA Pulse by SK · https://skakarh.com"
echo ""
