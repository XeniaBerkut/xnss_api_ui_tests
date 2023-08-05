import json
import time

import pytest

from ui.entities.user import User
from ui.pages.web_trading_page import WebTradingPage
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


def get_data():
    with open("test_registration_data.json", "r") as f:
        test_data = json.load(f)
    return test_data


@pytest.mark.parametrize("test_case", get_data(), ids=[data["test_case_title"] for data in get_data()])
def test_registration(driver: WebDriver, test_case: list):
    test_case["data"]["email"] = str(time.time_ns() % 1000000) + test_case["data"]["email"]
    user = User(**test_case["data"])
    home_page: HomePage = HomePage(driver)
    registration_page: RegistrationPage = home_page.go_to_registration_page(driver, RegistrationButtons.MENU.value)
    web_trading_page: WebTradingPage = registration_page.fill_form(driver, user)
    assert web_trading_page.driver.current_url == 'https://my.exness.com/webtrading/', \
        (f'Expected WebTradingPage, but was {web_trading_page.driver.current_url}. Maybe, because of the captcha,'
         f' as this is a pet project I cannot fix it')
