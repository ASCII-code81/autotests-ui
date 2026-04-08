from playwright.sync_api import sync_playwright, expect 

class RegPage:
    def __init__(self, page):
        self.p=page 
    @property 
    def btn(self): return self.p.get_by_test_id('registration-page-registration-button')

    @property 
    def btn(self): return self.p.get_by_test_id('registration-page-registration-button')

    @property 
    def email(self): return self.p.get_by_test_id('registration-form-email-input').locator('input')

    @property 
    def user(self): return self.p.get_by_test_id('registration-form-username-input').locator('input')

    @property 
    def pwd(self): return self.p.get_by_test_id('registration-form-password-input').locator('input')

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context=browser.new_context()
    page = RegPage(context.new_page())
    page.p.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    expect(page.btn).to_be_disabled()
    page.email.type("user.name@gmail.com", delay=50)
    page.user.type("username", delay=50)
    page.pwd.type("password", delay=50)
    expect(page.btn).to_be_enabled()