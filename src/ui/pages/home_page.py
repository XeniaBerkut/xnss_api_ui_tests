import logging

from ui.pages.base_page import BasePage

logger = logging.getLogger()


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'sign_up_btn_menu': ('XPATH', '//a[@data-param="menu-cta-1" and @data-testid="button:sign-up"]'),
        'sign_up_btn_header': ('XPATH', '//a[@data-param="header-cta-1" and @data-testid="button:sign-up"]'),
        'sign_up_btn_bottom': ('XPATH', '//a[@data-param="st-bottom-cta-1" and @data-testid="button:sign-up"]')
    }

    def go_to_registration_page(self, driver, registration_btn):
        logger.info(f'Click registration button {registration_btn}')
        self.registration_btn.click()
        return driver.current_url
