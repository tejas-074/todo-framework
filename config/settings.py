import os

ENV = os.getenv("TEST_ENV", "dev")

URLS = {
    "dev": "https://demo.playwright.dev/todomvc",
    "staging": "https://demo.playwright.dev/todomvc",
}

BASE_URL = URLS[ENV]