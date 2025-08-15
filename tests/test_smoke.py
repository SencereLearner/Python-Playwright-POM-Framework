import time
import allure
import pytest
from playwright.sync_api import expect
from pages.base_page import BasePage


@BasePage.log_time
@allure.title("Verify Contact Us text")
@pytest.mark.regression
def test_contact_us_displays_expected_message(base_page, home_page, contact_us_page):
    home_page.navigate_to_home_page()
    base_page.hover_over_header_menu_element("About Insureon")
    base_page.select_insurance_type("Contact Insureon")
    expect(contact_us_page.contact_us_ele).to_contain_text("For calls and emails, expect a response within 24 to 48 hours.")

@BasePage.log_time
@allure.title("Verify business class is present")
@pytest.mark.regression
def test_bus_class_search(base_page, home_page):
    home_page.navigate_to_home_page()
    home_page.click_get_quotes_button()
    home_page.enter_bus_class()
    home_page.verify_warn_message()

@BasePage.log_time
@allure.title("Open footer link in a new tab and verify title")
@pytest.mark.temp_test
def test_bus_class_search(home_page, footer_page):
    home_page.navigate_to_home_page()
    footer_page_title = "Privacy policy"
    new_footer_link_tab = footer_page.click_footer_element(footer_page_title)
    assert footer_page_title.lower() in new_footer_link_tab.title().lower()