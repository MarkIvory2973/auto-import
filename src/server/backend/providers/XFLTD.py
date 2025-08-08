from .base import *

class XFLTD(Provider):
    def __init__(self):
        permissions = ["clipboard-read"]
        url = "https://my.xfltd.org/#/login"
        super().__init__(permissions, url)
        
    def login(self, email, password):
        textboxEmail = self.page.get_by_role("textbox", name="Please enter your email")
        textboxPassword = self.page.get_by_role("textbox", name="Please enter your password")
        buttonLogin = self.page.get_by_role("button", name="Login")
        
        textboxEmail.fill(email)
        textboxPassword.fill(password)
        buttonLogin.click()
        
    def copy(self):
        buttonCopy = self.page.get_by_text("Copy")

        buttonCopy.click()
        subUrl = self.page.evaluate("navigator.clipboard.readText()")
        
        return subUrl