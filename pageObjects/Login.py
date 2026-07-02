class LoginPage:
    
    def __init__(self,page):
        self.page = page
        self.url = "https://www.rahulshettyacademy.com/client/auth/login"
        self.email = page.get_by_placeholder("email@example.com")
        self.password = page.get_by_placeholder("enter your passsword")
        self.login = page.get_by_role("button",name="Login")
        
    def navigate(self):
        self.page.goto(self.url)
    
    def user_login(self,userEmail,userPassword):
        self.email.fill(userEmail)
        self.password.fill(userPassword)
        self.login.click()

        
   