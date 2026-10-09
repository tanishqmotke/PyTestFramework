import pytest
from playwright.sync_api import Page,expect
@pytest.fixture(scope="function")
def _secondFixture():
    print("This is the second fixture")
    yield
    print("End of the second Fixture")

def test_testcase1(_preinitialSetup):
    print("This is test case 1")

def test_testcase2(_preinitialSetup):
    print("This is test case 2")

def test_testcase3(_preinitialSetup,_secondFixture):
    print("This is test case 3")
    print(_preinitialSetup)
    
    
#Verify if by entering the wrong credential the pop up occurs
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2s")

    page.get_by_role("radio",name="User").check()
    page.get_by_role("button",name="Okay").click()
    page.get_by_role("radio",name="Admin").check()
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_label("I Agree to the terms and conditions").check()
    page.get_by_role("button",name='Sign In').click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

