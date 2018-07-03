from TestData.Configuration import Config
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
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
            return Config.BASE_URL + self.URL
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
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)

    def is_radio_checked(self, locator):
        return self.get_element(locator).get_attribute("checked") == "true"

    def scroll_page(self, vertical_px, horizontal_px=0):
        self.driver.execute_script("window.scrollBy({}, {});".format(horizontal_px, vertical_px))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def click(self, locator_or_element):
        self.driver.switch_to_window(self.driver.current_window_handle)
        if isinstance(locator_or_element, WebElement):
            locator_or_element.click()
        else:
            self.get_element(locator_or_element).click()

    def type_text(self, locator, text, should_clear=True):
        self.driver.switch_to.window(self.driver.current_window_handle)
        element = self.get_element(locator)
        if should_clear:
            element.clear()
        element.send_keys(text)
        return element

    def _waiting_wrapper(self, expectation, locator_or_element, timeout, raise_on_fail=False):
        self.driver.implicitly_wait(0)
        try:
            return WebDriverWait(self.driver, timeout).until(expectation(locator_or_element))
        except TimeoutException as ex:
            if raise_on_fail:
                raise ex
            else:
                return False
        finally:
            self.driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)

    def wait_for_exist(self, locator, timeout=Config.WAITER_TIMEOUT):
        return self._waiting_wrapper(EC.presence_of_element_located, locator, timeout)

    def wait_for_not_exist(self, element, timeout=Config.WAITER_TIMEOUT):
        return self._waiting_wrapper(EC.staleness_of, element, timeout)

    def wait_for_visible(self, locator, timeout=Config.WAITER_TIMEOUT, raise_on_fail=False):
        return self._waiting_wrapper(EC.visibility_of_element_located, locator, timeout, raise_on_fail)

    def wait_for_not_visible(self, locator, timeout=Config.WAITER_TIMEOUT):
        return self._waiting_wrapper(EC.invisibility_of_element_located, locator, timeout)

    def get_elements_with_not_stale_waiting(self, action_method, timeout=Config.WAITER_TIMEOUT):
        self.driver.implicitly_wait(0)

        def excpectation(driver):
            try:
                return action_method(driver)
            except StaleElementReferenceException:
                return False

        try:
            return WebDriverWait(self.driver, timeout).until(excpectation)
        finally:
            self.driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
