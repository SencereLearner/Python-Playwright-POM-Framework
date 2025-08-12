import allure
import pytest
from playwright.sync_api import expect
from pages.base_page import BasePage


@BasePage.log_time
@allure.title("Verify Contact Us text")
@pytest.mark.regression
def test_check_contact_us_text(pages):
    pages['home_page'].navigate_to_home_page()
    pages['base_page'].hover_over_header_menu_element("About Insureon")
    pages['base_page'].select_insurance_type("Contact Insureon")
    expect(pages['contact_us_page'].contact_us_ele).to_contain_text("For calls and emails, expect a response within 24 to 48 hours.")


@BasePage.log_time
@allure.title("Verify business class is present")
@pytest.mark.temp_test
def test_bus_class_search(pages):
    pages['home_page'].navigate_to_home_page()
    pages['home_page'].click_get_quotes_button()
    pages['home_page'].enter_bus_class()
    pages['home_page'].verify_warn_message()