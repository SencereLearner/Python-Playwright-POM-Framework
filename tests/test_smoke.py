import allure
import pytest
from playwright.sync_api import expect
from conftest import home_page
from pages.base_page import BasePage


@BasePage.log_time
@allure.title("Verify Contact Us info")
@pytest.mark.temp_test
def test_navigate_to_selected_header_option(contact_us_page, base_page, home_page):
    home_page.navigate_to_home_page()
    base_page.hover_over_header_menu_element("About Insureon")
    base_page.select_insurance_type("Contact Insureon")
    expect(contact_us_page.contact_us_ele).to_contain_text("For calls and emails, expect a response within 24 to 48 hours.")