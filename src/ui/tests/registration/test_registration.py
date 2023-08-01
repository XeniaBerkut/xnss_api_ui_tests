import pytest

from ui.pages.home_page import HomePage
from ui.tests.registration.enums.registration_buttons import RegistrationButtons
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.mark.parametrize("btn", list(RegistrationButtons))
def test_registration_buttons(driver: WebDriver, btn: RegistrationButtons):
    home_page: HomePage = HomePage(driver)
    new_page_url = home_page.go_to_registration_page(driver, btn.value)
    assert new_page_url[:38] == 'https://my.exness.com/accounts/sign-up',\
        f'Expected registration page, but was {new_page_url}'
