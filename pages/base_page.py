import functools
from time import time
from playwright.sync_api import Page, expect, Dialog, Locator
from dotenv import load_dotenv
import os


def header_menu_locator(menu_type: str):
    return f"//a[@title='{menu_type}']"

def insurance_type_locator(insurance_type: str):
    return f"//a[@title='{insurance_type}']"


class BasePage:


    def __init__(self, page: Page):
        self.page = page

    header_title = 'h1'


    def open_page(self, url:str):
        self.page.goto(url=url)

    @property
    def current_url(self) -> str:
        return self.page.url

    @property
    def page_title(self) -> str:
        return self.page.title()

    @property
    def header_text(self) -> str:
        return self.page.locator(self.header_title).inner_text()

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def check_page_header_title_is(self, expected_text: str):
        actual_text = self.page.locator(self.header_title).inner_text()
        assert actual_text == expected_text, f"Expected header: '{expected_text}', but got: '{actual_text}'"

    def hover_over_header_menu_element(self, menu_type: str):
        self.find(header_menu_locator(menu_type)).hover()

    def select_insurance_type(self, insurance_type_title: str):
        self.find(insurance_type_locator(insurance_type_title)).click()

    def wait_for_element_to_load(self, locator: str, timeout: int = 5000) -> Locator:
        element = self.page.locator(locator)
        element.wait_for(state = 'visible', timeout = timeout)
        return element

    def wait_and_click(self, locator, timeout=7000, pause_ms=500):
        locator.wait_for(state='visible', timeout=timeout)
        expect(locator).to_be_enabled(timeout=timeout)
        self.page.wait_for_timeout(pause_ms)
        locator.scroll_into_view_if_needed()
        locator.click()

    load_dotenv()
    def get_env_var(self, name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise ValueError(f"Environment variable {name} is missing")
        return value

    # turns a method into a static method, not requiring self as its first parameter and doesn’t need access to the instance or class at all
    # used it here to not require self as the decorator could be used for both methods or functions
    @staticmethod
    def log_time(func):
        @functools.wraps(func)  # keeps functions original metadata like .__name__ and returns a function name instead of wrapper name
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            duration = time() - start
            print(f"{func.__name__} executed in {duration:.2f}s")
            return result
        return wrapper