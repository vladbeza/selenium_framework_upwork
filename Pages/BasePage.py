from TestData import Configuration
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):

    URL = None

    def __init__(self, driver):
        self.driver = driver

    def get_url(self):
        assert self.URL is not None, "URL should be assigned for Page object"
        if not self.URL.startswith('http'):
            return Configuration.BASE_URL + self.URL
        else:
            return self.URL

    def open_page(self):
        self.driver.get(self.get_url())

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

    def is_radio_checked(self, locator):
        return self.get_element(locator).get_attribute("checked") == "true"

    def scroll_page(self, vertical_px, horizontal_px=0):
        self.driver.execute_script("window.scrollBy({}, {});".format(horizontal_px, vertical_px))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        return element
