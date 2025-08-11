import allure
import pytest
from pages.base_page import BasePage


@BasePage.log_time
@allure.title("Navigate to Home page and check login error message")
@pytest.mark.smoke
def test_negative_login(home_page, login_page, login_sensitive_creds):
    home_page.navigate_to_home_page()
    home_page.click_log_in_link()
    login_page.enter_email(login_sensitive_creds['email'])
    login_page.enter_password(login_sensitive_creds.get('password'))
    login_page.click_login_button()
    login_page.validate_login_error_message()


