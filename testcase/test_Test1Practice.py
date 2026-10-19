import pytest
import json
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
with open('data/credentials.json') as f:
    credentails_json = json.load(f)
    test_data_list = credentails_json['user_credentials']

@pytest.mark.unit1
@pytest.mark.parametrize('getUserCredentails',test_data_list)
def test_coreLocators(page:Page,getUserCredentails):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    
    page.get_by_label("Username:").fill(getUserCredentails["userEmail"])
    page.get_by_label("Password:").fill(getUserCredentails["userPassword"])

    page.get_by_role("radio",name="User").check()
    page.get_by_role("button",name="Okay").click()
    page.get_by_role("radio",name="Admin").check()
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_label("I Agree to the terms and conditions").check()
    page.get_by_role("button",name='Sign In').click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

