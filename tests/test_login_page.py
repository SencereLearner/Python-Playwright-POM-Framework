import allure
import pytest
from pages.base_page import BasePage


@BasePage.log_time
@allure.title("Navigate to Home page and check login error message")
@pytest.mark.smoke
def test_negative_login(pages):
    pages['home_page'].navigate_to_home_page()
    pages['home_page'].click_log_in_link()
    pages['login_page'].enter_email(pages['base_page'].get_env_var("SENSITIVE_EMAIL"))
    pages['login_page'].enter_password(pages['base_page'].get_env_var("SENSITIVE_PASSWORD"))
    pages['login_page'].click_login_button()
    pages['login_page'].validate_login_error_message()


