

from playwright.sync_api import Page, expect
import re


# pytest --browser=chromium --headed
def test_first(page: Page):
    page.goto('https://www.google.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    expect(page).to_have_title(re.compile('^cat', re.IGNORECASE))


def test_by_role(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.get_by_role('menuitem', name="What's New").click()
    page.get_by_role('link', name='Search Terms').click()


def test_by_text(page: Page):
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Single UI Elements').click()


def test_by_label(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    field = page.get_by_label('Text string')
    field.press_sequentially('searching by label', delay=350)
    field.press('Control+a')
    field.press('Backspace')


def test_by_placeholder(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_placeholder('Submit me').fill('searching by placeholder')


def test_by_alt_text(page: Page):
    page.goto('https://epam.com')
    page.get_by_alt_text('The Next Evolution of Software Engineering').click()


def test_by_title(page: Page):
    page.goto('https://www.google.com/')
    page.get_by_title('Search').fill('searching by title')


def test_by_testid(page: Page):
    page.goto('https://www.airbnb.com/')
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()


def test_by_css_selector(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('.showcart').click()


def test_by_xpath(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('//*[@class="action showcart"]').click()