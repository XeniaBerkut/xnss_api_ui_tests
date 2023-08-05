from selenium.webdriver.support.wait import WebDriverWait

from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


class WebTradingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'welcome_dialog': ('XPATH', '//div[@data-testid="welcome-dialog"]')
    }

    def wait_welcome_dialog(self):
        self.welcome_dialog.visibility_of_element_located(timeout=10)

    def dismiss_notification(self):
        wait = WebDriverWait(self.driver, 100)
        try:
            alert = wait.until(EC.alert_is_present())
        except NoAlertPresentException:
            print("No alert dialog found or unable to handle the alert.")
        if alert:
            alert.dismiss()
