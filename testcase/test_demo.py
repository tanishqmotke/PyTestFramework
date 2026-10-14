import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_fixture():
    return "This is a fixture"

def test_demo(login_fixture,page:Page):
    print("This is the test case 1")
    page.goto("https://www.google.com")
    print(login_fixture)

def test_browser_demo(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")