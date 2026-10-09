# Create a fixture to login into the system
#select the Nokia product and add into the cart
import pytest
import re
from playwright.sync_api import Page,expect

@pytest.fixture(scope="function")
def login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("radio",name="User").check()
    page.get_by_role("button",name="Okay").click()
    page.get_by_role("radio",name="Admin").check()
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_label("I Agree to the terms and conditions").check()
    page.get_by_role("button",name='Sign In').click()
    yield
    print("The test is executed and logout from the profile")

@pytest.mark.smoke
def test_add_product_to_cart(login: None,page:Page):
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")
    expect(page).to_have_url(re.compile(r".*/shop"))
    products = ["Nokia Edge","Blackberry"]
    for product_name in products:
        product = page.locator("app-card").filter(has_text=product_name)
        product.get_by_role("button",name="Add").click()
            
    checkout = page.locator("a.nav-link.btn.btn-primary").filter(has_text="Checkout")
    count = 2
    expect(checkout).to_contain_text(f"Checkout ( {count} )")
    #expect(checkout).to_contain_text(f"Checkout ( {len(products)} )")
    checkout.click()
    expect(page.locator(".media-body")).to_have_count(2)
    product_items = page.locator("h4.media-heading")
    expect(product_items).to_have_text(products)

@pytest.mark.childwindow
def test_child_window_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    
    with page.expect_popup() as child_info:
     page.locator(".blinkingText").filter(has_text="Free Access").click()
     child_window = child_info.value
     child_window.wait_for_load_state()
     text = child_window.locator(".red").text_content()
     print(text)
     words = text.split(" at ")
     email = words[1].split(" ")[0]
     print(email)
    assert email == "mentor@rahulshettyacademy.com"
    
        
        
    