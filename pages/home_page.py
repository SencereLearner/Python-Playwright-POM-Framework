import random
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class HomePage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page)
        self._home_page_url = 'https://www.insureon.com/'
        self._log_in_ele = self.page.get_by_role('link', name='Log In')
        self._get_quotes_button_ele = self.page.locator('[data-test-id="navButtonCTA"]')
        self._warn_message = self.page.locator(".message_tauXM > strong")

    business_type_input_field = "//*[text()='Search for your business type']//following-sibling::div/input"
    business_classes_to_check = ["Non-Existing One", "Fake One", "Bogus One", "Deceptive One"]

    @property
    def home_page_url(self):
        return self._home_page_url

    @property
    def log_in_ele(self):
        return self._log_in_ele

    @property
    def get_quotes_button_ele(self):
        return self._get_quotes_button_ele

    @property
    def warn_message(self):
        return self._warn_message

    @allure.step("Navigating to home page")
    def navigate_to_home_page(self) -> None:
        self.open_page(self.home_page_url)

    @allure.step("Clicking log in link")
    def click_log_in_link(self) -> None:
        self.log_in_ele.click()

    @allure.step("Clicking Get Quotes button")
    def click_get_quotes_button(self) -> None:
        self.wait_and_click(self.get_quotes_button_ele)

    @allure.step("Open Get Quotes menu and enter randomly selected bus class")
    def enter_bus_class(self) -> None:
        selected_bus_class = random.choice(self.business_classes_to_check)
        print("Selected Business Class: ", selected_bus_class)
        self.wait_for_element_to_load(self.business_type_input_field).fill(selected_bus_class)

    def verify_warn_message(self) -> None:
        expect(self.warn_message).to_contain_text("Sorry, we couldn’t find")




