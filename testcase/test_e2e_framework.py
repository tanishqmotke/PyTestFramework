import json
import pytest
from playwright.sync_api import Playwright
from pageobjects.Login import LoginPage
from utils.test_apibase import APIUtils

 #This method will convert an json to the Python object i.e. List, Dictonaries
with open('data/credentials.json') as f:
        test_data = json.load(f)  
        print(f"This is the test_data: {test_data}")
        user_cred_list = test_data['user_credentials']

@pytest.mark.parametrize("credentials",user_cred_list)
def test_e2e_web_api(playwright:Playwright,credentials):
   
    username = credentials["userEmail"]
    password = credentials["userPassword"]
    
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    #create_order
    web_api = APIUtils()
    order_id = web_api.create_order(playwright,credentials)
    
    loginPage = LoginPage(page)
    loginPage.navigate()
    dasboard = loginPage.user_login(username,password)
    orderHistory = dasboard.navigate_to_Orders()
    
    orderSummary = orderHistory.click_on_OrderId_view_button(order_id)
   
    orderSummary.validate_summary()