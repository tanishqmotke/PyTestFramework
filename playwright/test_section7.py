from time import sleep

from playwright.sync_api import Page, expect

def test_morevalidation(page:Page):
    
    #To hide and to be visible
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    
    #to handle dialog box
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    
    #to handle frames 
    pFrame = page.frame_locator("#courses-iframe")
    courses_link = pFrame.get_by_role("link",name="Courses")
    print(courses_link.count())
    courses_link.nth(1).click()
    
    page.get_by_role("combobox").select_option("Option3")
    
    
    