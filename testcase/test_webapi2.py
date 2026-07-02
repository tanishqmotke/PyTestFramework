from time import sleep

from playwright.sync_api import Page, Playwright, expect

from utils.test_apibase import APIUtils

fakePayloadOrderPurchase = {"data":[], "message": "No Orders"}
def mocked_response(route):
    route.fulfill(
        json = fakePayloadOrderPurchase
    )
def test_no_order_validation(page:Page):
    
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",mocked_response)
    page.goto("https://www.rahulshettyacademy.com/client/auth/login")
    page.get_by_placeholder("email@example.com").fill("tanishqmotke110@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Pass@123")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button",name="  ORDERS").click()
    no_order_text = page.locator(".mt-4").text_content()
    print(no_order_text)
    
def mocked_request(route):
    route.continue_(url="https://www.rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a461892cd73adf7e58b67ae")

def test_unauthorised_access(page:Page):

    page.goto("https://www.rahulshettyacademy.com/client/auth/login")
    page.route("https://www.rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",mocked_request)
    page.get_by_placeholder("email@example.com").fill("tanishqmotke110@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Pass@123")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button",name="  ORDERS").click()
    page.get_by_role("button",name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)
    

def test_add_session_cookie(playwright:Playwright):
    api = APIUtils()
    getToken = api.user_login(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://www.rahulshettyacademy.com/client")
    page.get_by_role("button",name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
    