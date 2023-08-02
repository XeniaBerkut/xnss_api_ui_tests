import logging

from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.pages.registration_page import RegistrationPage

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

        logger.info('Check if there are only two active pages')
        active_pages = driver.window_handles
        assert len(active_pages) == 2, f'Expected two active pages, but was {len(active_pages)}'

        logger.info("Check if HomePage is still active so RegistrationPage is open in a new window ")
        assert driver.current_url == 'https://www.exness.com/', \
            f'Expected HomePage is active, but was {driver.current_url}'

        logger.info('Switch to RegistrationPage')
        driver.switch_to.window(active_pages[1])
        return RegistrationPage(driver)
