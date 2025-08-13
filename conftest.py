from pages.base_page import BasePage
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest
from playwright.sync_api import Page


@pytest.fixture()
def base_page(page):
    return BasePage(page)

@pytest.fixture()
def home_page(page):
    return HomePage(page)

@pytest.fixture()
def login_page(page):
    return LoginPage(page)

@pytest.fixture()
def contact_us_page(page):
    return ContactUsPage(page)

# to run the tests: pytest -m temp_test -s or pytest -m-s
# to run with allure: 1)rm -rf allure-results 2) pytest --alluredir=allure-results 3) allure serve allure-results
# for cross browser testing: pytest --browser webkit --browser firefox --browser chromium (will run in 3 browsers 1 by 1)
# wait for specific element: myEle.wait_for(state='visible', timeout=5000)