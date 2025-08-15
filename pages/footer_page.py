from pages.base_page import BasePage
from playwright.sync_api import Page

class FooterPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page)
        self.privacy_policy = self.page.get_by_role("link", name = "Privacy policy")


    def footer_link_xpath(self, footer_option: str) -> str:
        return f"//a[text()='{footer_option}']"

    def click_footer_element(self, footer_option):
        return self.open_link_in_new_tab(self.footer_link_xpath(footer_option))
