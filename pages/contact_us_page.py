from xml.sax.xmlreader import Locator
from playwright.sync_api import Page
from pages.base_page import BasePage


class ContactUsPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page)
        self._contact_us_ele = self.page.locator("[data-test-id='LegalDescriptor'] > div")

    @property
    def contact_us_ele(self) -> Locator:
        return self._contact_us_ele


