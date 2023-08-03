import pytest

from ui.tests.conftest import driver, logger
from ui.pages.home_page import HomePage
from ui.enums.registration_buttons import RegistrationButtons
from ui.pages.registration_page import RegistrationPage
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.mark.parametrize("btn", list(RegistrationButtons))
def test_registration_buttons(driver: WebDriver, btn: RegistrationButtons):
    home_page: HomePage = HomePage(driver)

    logger.info(f'Go to the Registration page by clicking {btn}')
    registration_page: RegistrationPage = home_page.go_to_registration_page(driver, btn.value)

    logger.info('Check if url of RegistrationPage is correct')
    registration_page_url: str = registration_page.driver.current_url
    expected_static_url_part: str = 'https://my.exness.com/accounts/sign-up'
    assert registration_page_url.startswith(expected_static_url_part),\
        f'Expected RegistrationPage, but was {registration_page_url}'
