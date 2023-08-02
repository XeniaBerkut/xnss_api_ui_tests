import pytest

from ui.tests.conftest import driver, logger
from ui.pages.home_page import HomePage
from ui.enums.registration_buttons import RegistrationButtons
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.mark.parametrize("btn", list(RegistrationButtons))
def test_registration_buttons(driver: WebDriver, btn: RegistrationButtons):
    home_page: HomePage = HomePage(driver)
    logger.info("Open registration page and return driver.window_handles")
    active_pages = home_page.go_to_registration_page(driver, btn.value)
    logger.info("Check if there are only two active pages and check their urls")
    assert len(active_pages) == 2
    assert driver.current_url == 'https://www.exness.com/'
    driver.switch_to.window(active_pages[1])
    new_url = driver.current_url

    assert new_url[:38] == 'https://my.exness.com/accounts/sign-up',\
        f'Expected registration page, but was {active_pages}'
