from . import *

class Provider:
    def __init__(self, permissions, url):
        self.permissions = permissions
        self.url = url
        
    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.context = self.browser.new_context(permissions=self.permissions)
        self.page = self.context.new_page()
        
        self.page.goto(self.url)
        
        return self
        
    def __exit__(self, *_):
        self.page.close()
        self.context.close()
        self.browser.close()
        self.playwright.stop()