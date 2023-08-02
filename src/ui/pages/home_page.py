import logging

from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage

logger = logging.getLogger()


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'sign_up_btn_menu': (By.XPATH, "//a[contains(@data-param, 'menu') and @data-testid='button:sign-up']"),
        'sign_up_btn_header': (By.XPATH, '//a[contains(@data-param, "header") and @data-testid="button:sign-up"]'),
        'sign_up_btn_bottom': (By.XPATH, '//a[contains(@data-param, "bottom") and @data-testid="button:sign-up"]')
    }

    def go_to_registration_page(self, driver, registration_btn):
        logger.info(f'Click registration button {registration_btn}')
        element = self.driver.find_element(*self.locators[registration_btn])
        element.click()
        logger.info('The registration button was clicked')
        return driver.window_handles
