from pages.base_page import BasePage
import allure
import pytest


@BasePage.log_time
@allure.title("Navigate to selected header menu option")
@pytest.mark.smoke
def test_nav_to_header_menu_option():
    pass