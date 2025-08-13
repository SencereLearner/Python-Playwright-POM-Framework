from xml.sax.xmlreader import Locator
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page)
        self._email_address_input = self.page.locator('#email')
        self._password_address_input = self.page.locator('#password')
        self._login_button = self.page.get_by_test_id('login-page-login-button')
        self._error_message = self.page.get_by_text('Email address or password is not valid', exact=True)

    @property
    def email_address_input(self) -> Locator:
        return self._email_address_input

    @property
    def password_address_input(self) -> Locator:
        return self._password_address_input

    @property
    def login_button(self) -> Locator:
        return self._login_button

    @property
    def error_message(self) -> Locator:
        return self._error_message

    @allure.step("Entering email")
    def enter_email(self, email: str) -> None:
        self.email_address_input.fill(email)

    @allure.step("Entering password")
    def enter_password(self, password: str) -> None:
        self.password_address_input.fill(password)

    @allure.step("Clicking Login button")
    def click_login_button(self) -> None:
        self.login_button.click()

    @allure.step("Validating error message")
    def validate_login_error_message(self) -> None:
        print("Login error message: ", self.error_message.inner_text())
        expect(self.error_message).to_have_text('Email address or password is not valid')



