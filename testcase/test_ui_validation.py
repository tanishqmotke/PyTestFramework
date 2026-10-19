# Create a fixture to login into the system
#select the Nokia product and add into the cart
import pytest
import re
from pageobjects.product_cart import ProductCart
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
    products = ["Nokia Edge","Blackberry"]
    
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")
    expect(page).to_have_url(re.compile(r".*/shop"))
    
    product_cart = ProductCart(page)
    for product in products:
         product_cart.add_product_to_cart(product)

    checkout_count = product_cart.checkout()        
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
    #words = text.split(" at ")
    # email = words[1].split(" ")[0]
     #print(email)
    #assert email == "mentor@rahulshettyacademy.com"
    
        
@pytest.mark.locatorpractice
def test_locator_practice(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    
    radio = page.locator("input[value='radio2']")
    radio.check()
    expect(radio).to_be_checked()
    
    country = page.get_by_placeholder("Type to Select Countries")
    country.press_sequentially("India")
    page.locator(".ui-menu-item").get_by_text("India", exact=True).click()
    expect(country).to_have_value("India")
    
    
    dropdown = page.locator("#dropdown-class-example")
    dropdown.select_option("option3")
    expect(dropdown).to_have_value("option3")

    checkbox = page.locator("#checkBoxOption3")
    checkbox.check()
    expect(checkbox).to_be_checked()
    
    with page.expect_popup() as childwindowInfo:
        page.get_by_role("button",name="Open Window").click()
        childwindow = childwindowInfo.value
        message = childwindow.locator("h1").first.text_content()
        print(message)
        childwindow.close()
        assert childwindow.is_closed()
    
    with page.expect_popup() as childtabInfo:
            page.locator("#opentab").click()
            childwindow = childtabInfo.value
            message = childwindow.locator("h1").first.text_content()
            print(message)
            childwindow.close()
            assert childwindow.is_closed()
    
    enter_name = page.locator("#name")
    enter_name.fill("Tanishq")
    expect(enter_name).to_have_value("Tanishq")
    
    page.on("dialog",lambda dialog:dialog.accept())
    alert_button = page.locator("#alertbtn")
    alert_button.click()
    
    pageframe = page.frame_locator("#courses-iframe")
    title = pageframe.locator("h2>span").first.text_content()
    print(title)
    
@pytest.mark.smoke
def test_table_practice(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    
    #Print the Position of the person in the 4th row.
    table = page.locator(".tableFixHead #product")
    row = table.locator("tbody tr").nth(3)
    position = row.locator("td").nth(1).text_content()
    print(position)
    
    #Task 2 – Lookup by value
    # Given the name “Jack”, print his City and Amount in one line, e.g. Jack lives in ___ and paid ___.
    row = table.locator("tbody tr").filter(has_text="Jack")
    position = row.locator("td").nth(1).text_content()
    city = row.locator("td").nth(2).text_content()
    print(f"Jack lives in {city} and paid {position}")
    
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()