import random
import time

import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class HomePage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page)
        self.home_page_url = 'https://www.insureon.com/'
        self.log_in_ele = self.page.get_by_role('link', name='Log In')
        self.get_quotes_button_ele = self.page.locator('[data-test-id="navButtonCTA"]')
        self.warn_message = self.page.locator(".message_tauXM > strong")

    business_type_input_field = "//*[text()='Search for your business type']//following-sibling::div/input"
    business_classes_to_check = ["Non-Existing One", "Fake One", "Bogus One", "Deceptive One"]

    @allure.step("Navigating to home page")
    def navigate_to_home_page(self):
        self.open_page(self.home_page_url)

    @allure.step("Clicking log in link")
    def click_log_in_link(self):
        self.log_in_ele.click()

    @allure.step("Clicking Get Quotes button")
    def click_get_quotes_button(self):
        self.wait_and_click(self.get_quotes_button_ele)

    @allure.step("Open Get Quotes menu and enter randomly selected bus class")
    def enter_bus_class(self):
        selected_bus_class = random.choice(self.business_classes_to_check)
        print("Selected Business Class: ", selected_bus_class)
        self.wait_for_element_to_load(self.business_type_input_field).fill(selected_bus_class)

    def verify_warn_message(self):
        expect(self.warn_message).to_contain_text("Sorry, we couldn’t find")




