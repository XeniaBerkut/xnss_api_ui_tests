import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        super().__init__()
        self.driver = driver

    def wait_element_is_visible(self, element_locator: tuple, timeout: int):
        logging.info(f"Wait for {element_locator} to be visible")
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(element_locator))
