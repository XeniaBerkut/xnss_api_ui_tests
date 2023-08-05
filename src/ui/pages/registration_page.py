import logging

from selenium.webdriver import Keys

from ui.entities.user import User
from ui.pages.base_page import BasePage
from ui.pages.web_trading_page import WebTradingPage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'country': ('NAME', "country"),
        'email': ('NAME', "email"),
        'password': ('NAME', "password"),
        'sing_up_btn': ('XPATH', '//*[@id="mui-6"]'),
        'captcha': ('ID', '//*[@id="recaptcha-anchor-label"]')
    }

    def fill_form(self, driver,  user: User):
        logging.info('Chose country: {}'.format(user.country))
        print(self.country.get_text())
        self.country.send_keys(user.country)
        self.country.send_keys(Keys.RETURN)
        logging.info('Fill email'.format(user.email))
        self.email.send_keys(user.email)
        logging.info('Fill password')
        self.password.send_keys(user.password)
        logging.info('Confirm registration')
        self.sing_up_btn.click()
        web_trading_page = WebTradingPage(driver)
        web_trading_page.dismiss_notification()

        web_trading_page.wait_welcome_dialog()
        return web_trading_page
