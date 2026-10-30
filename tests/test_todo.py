from playwright.sync_api import Page, expect

def test_add_one_todo(todo_page: TodoPage):
    todo_page.add("Buy milk")
    expect(todo_page.items).to_have_count(1)
    expect(todo_page.items).to_have_text("Buy milk")

def test_add_two_todos(todo_page: TodoPage):
    todo_page.add("Buy milk")
    todo_page.add("Pay bills")
    expect(todo_page.items).to_have_count(2)
   