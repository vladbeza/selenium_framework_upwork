from TestData import Configuration
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):

    URL = None

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        assert self.URL is not None, "URL should be assigned for Page object"
        if not self.URL.startswith('http'):
            self.URL = Configuration.BASE_URL + self.URL
        self.driver.get(self.URL)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_exist(self, locator):
        self.driver.implicitly_wait(1)
        try:
            element = self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(Configuration.IMPLICIT_WAIT_TIMEOUT)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return element
