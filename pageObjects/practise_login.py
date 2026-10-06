class PractiseLoginPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://rahulshettyacademy.com/loginpagePractise/"
        self.username = page.get_by_role("textbox", name="Username:")
        self.password = page.get_by_role("textbox", name="Password:")
        self.terms_checkbox = page.get_by_role("checkbox", name="I Agree to the terms and conditions")
        self.sign_in = page.get_by_role("button", name="Sign In")
        self.error_message = page.get_by_text("is no longer valid")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.terms_checkbox.check()
        self.sign_in.click()
