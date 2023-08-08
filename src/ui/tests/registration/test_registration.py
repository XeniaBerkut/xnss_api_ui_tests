import json
import logging
import time

import pytest

from ui.entities.user import User
from ui.enums.registration_controls_texts import RegistrationControlsTexts
from ui.pages.web_trading_page import WebTradingPage
from ui.tests.conftest import driver, logger
from ui.pages.home_page import HomePage
from ui.enums.registration_buttons import RegistrationButtons
from ui.pages.registration_page import RegistrationPage
from selenium.webdriver.chrome.webdriver import WebDriver


def get_data(test_data_file_name: str) -> list[dict]:
    with open(test_data_file_name, "r") as f:
        test_data = json.load(f)
    return test_data


@pytest.mark.priority(2)
@pytest.mark.parametrize("test_case",
                         get_data("test_registration_data_user.json"),
                         ids=[data["test_case_title"] for data in get_data("test_registration_data_user.json")])
def test_registration(driver: WebDriver, test_case: dict):
    driver.get("https://my.exness.com/accounts/sign-up")

    test_case["data"]["email"] = str(time.time_ns() % 1000000) + test_case["data"]["email"]
    user = User(**test_case["data"])
    registration_page: RegistrationPage = RegistrationPage(driver)

    web_trading_page: WebTradingPage = registration_page.fill_form(driver, user)
    web_trading_page.wait_welcome_dialog()
    assert web_trading_page.driver.current_url == 'https://my.exness.com/webtrading/', \
        (f'Expected WebTradingPage, but was {web_trading_page.driver.current_url}. Maybe, because of the captcha,'
         f' as this is a pet project I cannot fix it')


@pytest.mark.priority(1)
@pytest.mark.parametrize("test_case",
                         get_data("test_registration_data_pwd_controls.json"),
                         ids=[data["test_case_title"] for data in get_data("test_registration_data_pwd_controls.json")])
def test_registration_form_password_controls(driver: WebDriver, test_case: dict):
    logging.info('Go to the RegistrationPage')
    driver.get("https://my.exness.com/accounts/sign-up")

    logging.info(f'Create user from test data {test_case["data"]}')
    user = User(**test_case["data"])

    registration_page: RegistrationPage = RegistrationPage(driver)
    logging.info('Fill registration page')
    registration_page: RegistrationPage = registration_page.fill_form(driver, user)

    logging.info('Check if registration is not completed and we are still on the RegistrationPage')
    registration_page_url: str = driver.current_url
    expected_static_url_part: str = 'https://my.exness.com/accounts/sign-up'
    assert registration_page_url.startswith(expected_static_url_part), \
        f'Expected RegistrationPage, but was {registration_page_url}'

    for control in test_case["controlColor"]:
        expected_color = test_case["controlColor"][control]
        control_text: str = RegistrationControlsTexts[control].value
        logging.info(f"Get color of the control text '{control_text}'")
        control_text_color: str = registration_page.get_control_color(registration_page, control_text)
        logging.info('Check if color is correct')
        assert control_text_color == expected_color, f'Expected {expected_color} color, but was {control_text_color}'


@pytest.mark.parametrize("btn", list(RegistrationButtons))
def test_registration_buttons(driver: WebDriver, btn: RegistrationButtons):
    driver.get("https://www.exness.com/")
    home_page: HomePage = HomePage(driver)

    logger.info(f'Go to the Registration page by clicking {btn}')
    registration_page: RegistrationPage = home_page.go_to_registration_page(driver, btn.value)

    logger.info('Check if url of RegistrationPage is correct')
    registration_page_url: str = registration_page.driver.current_url
    expected_static_url_part: str = 'https://my.exness.com/accounts/sign-up'
    # TODO use url_contains from EC
    assert registration_page_url.startswith(expected_static_url_part),\
        f'Expected RegistrationPage, but was {registration_page_url}'
