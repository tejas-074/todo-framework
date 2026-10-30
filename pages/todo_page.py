from playwright.sync_api import Page


class TodoPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_todo = page.get_by_placeholder("What needs to be done?")
        self.items = page.get_by_test_id("todo-item")

    def open(self, base_url):
        self.page.goto(base_url)

    def add(self, text):
        self.new_todo.fill(text)
        self.new_todo.press("Enter")