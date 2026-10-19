from playwright.sync_api import Playwright, expect

from utils.test_apibase import APIUtils

def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    #create_order
    web_api = APIUtils()
    order_id = web_api.create_order(playwright)
    
    page.goto("https://www.rahulshettyacademy.com/client/auth/login")
    page.get_by_placeholder("email@example.com").fill("tanishqmotke110@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Pass@123")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button",name="  ORDERS").click()
    
    order_id_position = page.locator("tr").filter(has_text=order_id)
    order_id_position.locator("td").get_by_role("button",name="View").click()
    expect(page.get_by_text("ORDER SUMMARY")).to_be_visible()