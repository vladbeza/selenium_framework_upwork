from TestData import Configuration
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

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

    def click(self, locator_or_element):
        self.driver.switch_to_window(self.driver.current_window_handle)
        if isinstance(locator_or_element, WebElement):
            locator_or_element.click()
        else:
            self.get_element(locator_or_element).click()

    def type_text(self, locator, text, should_clear=True):
        self.driver.switch_to_window(self.driver.current_window_handle)
        element = self.get_element(locator)
        if should_clear:
            element.clear()
        element.send_keys(text)

    def wait_for_exist(self, locator, timeout=Configuration.WAITER_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_not_exist(self, element, timeout=Configuration.WAITER_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.staleness_of(element))

    def wait_for_visible(self, locator, timeout=Configuration.WAITER_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_not_visible(self, locator, timeout=Configuration.WAITER_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))