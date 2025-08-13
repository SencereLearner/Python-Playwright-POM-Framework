import allure
import pytest
from pages.base_page import BasePage


@BasePage.log_time
@allure.title("Navigate to Home page and check login error message")
@pytest.mark.smoke
def test_negative_login(base_page, home_page, login_page):
    home_page.navigate_to_home_page()
    home_page.click_log_in_link()
    login_page.enter_email(base_page.get_env_var("SENSITIVE_EMAIL"))
    login_page.enter_password(base_page.get_env_var("SENSITIVE_PASSWORD"))
    login_page.click_login_button()
    login_page.validate_login_error_message()


