
Python with Playwright Page Object Model (POM) Framework

Techniques & Features used in the project:

1. Requirements.txt – Keeps track of all project dependencies for easy transfer and setup.
2. Pytest fixtures – Used in conftest.py to provide reusable page object instances (base_page, home_page, login_page, contact_us_page).
3. Pytest-playwright built-in page fixture – No manual browser initialization needed.
4. POM structure – Each page (BasePage, HomePage, LoginPage, ContactUsPage) is its own class with locators, actions and verifications.
5. Inheritance – BasePage provides shared actions, utilities and common locators to all child page classes.
6. Properties (@property) – Used to expose locators in a clean, read-only manner.
7. Custom helper methods – wait_and_click, wait_for_element_to_load, etc., wrap PW actions with waits and conditions.
8. Environment variable management – get_env_var loads sensitive data from .env for credentials and other secrets.
9. Custom decorators – @BasePage.log_time measures and reports test execution time with Allure added to it.
10. Allure reporting – @allure.step annotations for logging methods actions. @allure.title for readable test titles.
11. Parameterized locators – Methods that build locators dynamically using input arguments to combine locators of the same group or web page section.
12. Custom assertions – Encapsulated in methods like check_page_header_title_is and verify_warn_message for consistency.
13. Randomized test data – random.choice() used for generating dynamic input (some fake business classes in HomePage).
14. Pytest markers – smoke, regression, temp_test for grouping and selective execution.
15. Configuration file (pytest.ini) – Stores CLI defaults (timeouts, logging, browser mode) and marker registration.
16. Encapsulation – Page locators are protected (self._locator_name) with public getters for controlled access.
17. Playwright assertions – Using expect() for robust, Playwright-native checks.
18. Sync Playwright API – Using playwright.sync_api for synchronous test flow.