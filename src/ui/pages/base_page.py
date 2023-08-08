import logging

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        super().__init__()
        self.driver = driver

    def wait_element_is_interactable(self, element_locator: tuple, timeout: int):
        logging.info(f"Wait for {element_locator} to be visible and clickable")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element_locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element_locator))
            logging.info("Element is clickable")
        except TimeoutException:
            logging.warning(f"The element {element_locator} is not clickable. Refreshing the page...")
            self.driver.refresh()
            logging.warning("The page was refreshed")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element_locator))
            logging.warning(f'{element_locator} is visible')
            actions = ActionChains(self.driver)
            element = self.driver.find_element(element_locator[0], element_locator[1])
            logging.warning('Move to element')
            actions.move_to_element(element).perform()
            logging.warning('Wait element is clickable')
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element_locator))


