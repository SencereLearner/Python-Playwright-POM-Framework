import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page)
        self.email_address_input = self.page.locator('#email')
        self.password_address_input = self.page.locator('#password')
        self.login_button = self.page.get_by_test_id('login-page-login-button')
        self.error_message = self.page.get_by_text('Email address or password is not valid', exact=True)


    @allure.step("Entering email")
    def enter_email(self):
        return self.email_address_input.fill('my@email.com')

    @allure.step("Entering password")
    def enter_password(self):
        return self.password_address_input.fill('login123')

    @allure.step("Clicking Login button")
    def click_login_button(self):
        return self.login_button.click()

    @allure.step("Validating error message")
    def validate_login_error_message(self):
        print("Login error message: ", self.error_message.inner_text())
        expect(self.error_message).to_have_text('Email address or password is not valid')



