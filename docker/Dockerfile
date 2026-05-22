FROM python:3.12-slim

# ── System dependencies ───────────────────────────────────────────────────────
RUN apt-get update && apt-get install -y \
    wget curl gnupg unzip \
    google-chrome-stable \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# ── Working directory ─────────────────────────────────────────────────────────
WORKDIR /app

# ── Python dependencies ───────────────────────────────────────────────────────
COPY requirements-ci.txt .
RUN pip install --no-cache-dir -r requirements-ci.txt

# ── Copy project ──────────────────────────────────────────────────────────────
COPY . .

# ── Environment ───────────────────────────────────────────────────────────────
ENV HEADLESS=true
ENV BROWSER=chrome
ENV BASE_URL=https://the-internet.herokuapp.com
ENV PYTHONUNBUFFERED=1

# ── Run tests ─────────────────────────────────────────────────────────────────
CMD ["pytest", "tests/", "--headless", "-n", "2", "--tb=short", \
     "--html=reports/report.html", "--self-contained-html"]
