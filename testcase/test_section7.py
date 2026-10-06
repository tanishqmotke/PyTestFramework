#This is made by the Claude Code
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
    
    #to handle WebTable
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).text_content().strip()=="Price":
            price_col = index
            print(f"The column for the Price is {price_col}")
            break
    
    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(price_col)).to_have_text("37")
         
    
    