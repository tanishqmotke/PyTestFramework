import re

from playwright.sync_api import Page, expect  # type: ignore

def test_uivalidation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign in").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button",name="Add").click()
    page.locator("app-card").filter(has_text="Samsung Note 8").get_by_role("button",name="Add").click()
    checkout = page.get_by_text("Checkout")
    print(checkout)
    checkout.click()
   # expect(checkout).to_contain_text("Checkout (2)")
    #page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.get_by_text("iphone X")).to_be_visible()
    expect(page.get_by_text("Samsung Note 8")).to_be_visible()

def test_child_window(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
      
    with page.expect_popup() as pageInfo: 
        page.get_by_role("link",name="Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_window = pageInfo.value
        text = child_window.locator(".red").text_content()
        print(text)
        email = text.split("at")[1].split("with")[0].strip()
        print(email)
    page.get_by_label("Username:").fill(email)
    
      
    