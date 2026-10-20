import pytest
from pytest_bdd import given, scenarios, then, parsers, when

from pageobjects.login import LoginPage
from utils.test_apibase import APIUtils

scenarios('orderTransaction.feature')

@pytest.fixture
def shared_fixture():
    return{}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright,username,password,shared_fixture):
    credentials={}
    credentials["userEmail"]=username
    credentials["userPassword"]=password
        
        #create_order
    web_api = APIUtils()
    order_id = web_api.create_order(playwright,credentials)
    shared_fixture['order_id'] = order_id

@given('the user is on landing page')
def user_on_landing_page(browser_instance,shared_fixture):
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    shared_fixture['loginPage']= loginPage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username,password,shared_fixture):
    login_page = shared_fixture['loginPage']
    dashboard = login_page.user_login(username,password)
    shared_fixture['dashboard']= dashboard

@when('navigate to order page')
def navigate_to_order_page(shared_fixture):
    dashboard = shared_fixture['dashboard']
    orderHistory = dashboard.navigate_to_Orders()
    shared_fixture['orderHistory'] = orderHistory

@then('select the orderId and order message is successfully displayeds')
def select_orderId_and_validate(shared_fixture):
    order_history = shared_fixture['orderHistory']
    orderSummary = order_history.click_on_OrderId_view_button(shared_fixture['order_id'])
    orderSummary.validate_summary()