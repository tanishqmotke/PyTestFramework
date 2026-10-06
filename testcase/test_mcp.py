from playwright.sync_api import expect
from pageobjects.practise_login import PractiseLoginPage


def test_practise_login(browser_instance):
    loginPage = PractiseLoginPage(browser_instance)
    loginPage.navigate()
    loginPage.login("rahulshettyacademy", "learning")

    # Observed manually: the site rejects the old password "learning"
    expect(loginPage.terms_checkbox).to_be_checked()
    expect(loginPage.error_message).to_be_visible()
