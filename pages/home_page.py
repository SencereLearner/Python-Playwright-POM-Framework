import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class HomePage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page)
        self.home_page_url = 'https://www.insureon.com/'
        self.log_in_ele = self.page.get_by_role('link', name='Log In')


    @allure.step("Navigating to home page")
    def navigate_to_home_page(self):
        self.open_page(self.home_page_url)

    @allure.step("Clicking log in link")
    def click_log_in_link(self):
        return self.log_in_ele.click()


