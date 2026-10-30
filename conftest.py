import pytest
from playwright.sync_api import Page
from config.settings import BASE_URL
from pages.todo_page import TodoPage


@pytest.fixture
def todo_page(page: Page):
    tp = TodoPage(page)
    tp.open(BASE_URL)
    return tp