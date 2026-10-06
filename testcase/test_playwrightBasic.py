import time

from playwright.sync_api import Page, expect
import pytest

def test_testcase1(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")
    
def test_testcase6(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")


def test_testcase2(page:Page):
    page.goto("https://www.google.com") 

@pytest.mark.smoke
def test_testcase3(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@g830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign in").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    
def test_initialCheck(_preinitialSetup):
    print("This is the first test created")