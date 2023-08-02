import pytest

from ui.tests.conftest import driver, logger
from ui.pages.home_page import HomePage
from ui.enums.registration_buttons import RegistrationButtons
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.mark.parametrize("btn", list(RegistrationButtons))
def test_registration_buttons(driver: WebDriver, btn: RegistrationButtons):
    home_page: HomePage = HomePage(driver)

    logger.info(f'Go to the Registration page by clicking {btn}')
    registration_page = home_page.go_to_registration_page(driver, btn.value)

    logger.info('Check if url of RegistrationPage is correct')
    registration_page_url = registration_page.driver.current_url
    static_url_part = registration_page_url[:38]
    assert static_url_part == 'https://my.exness.com/accounts/sign-up',\
        f'Expected registration page, but was {registration_page_url}'
