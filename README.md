# Playwright Python Todo Framework

![Tests](https://github.com/tejas-074/todo-framework/actions/workflows/tests.yml/badge.svg)

End-to-end tests for the TodoMVC demo app, run on three browsers and a phone-sized screen.

## Design decisions
- **Page Object Model**: `pages/todo_page.py` hides locators, so tests read like plain English.
- **Config in one place**: `config/settings.py` holds the URL, chosen by the `TEST_ENV` variable.
- **Cross-browser CI**: a GitHub Actions matrix runs the suite on chromium, firefox and webkit in parallel.
- **Reporting from day one**: `pytest.ini` writes an HTML report, screenshots and traces on failure.

## Run locally
```
pip install -r requirements.txt
playwright install
pytest --browser chromium --browser firefox --browser webkit
pytest --device "iPhone 13"
```