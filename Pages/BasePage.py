import allure

from TestData.Configuration import Config
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement


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
        with allure.step("Open page {}".format(self.__class__.__name__)):
            self.driver.get(self.get_url())

    def is_url_opened(self, time_to_wait=Config.WAITER_TIMEOUT):
        return self._waiting_wrapper(lambda driver: driver.current_url == self.get_url(), None, time_to_wait)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_elements_with_waiting(self, locator, timeout=Config.WAITER_TIMEOUT):
        if self._waiting_wrapper(lambda driver: driver.find_elements(*locator), locator, timeout, True):
            return self.get_elements(locator)

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

    @allure.step("Scroll page in {1} pixels vertically, {2} pixels horizontally")
    def scroll_page(self, vertical_px, horizontal_px=0):
        self.driver.execute_script("window.scrollBy({}, {});".format(horizontal_px, vertical_px))

    @allure.step("Scroll page to element {1}")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def click(self, locator_or_element):
        self.driver.switch_to_window(self.driver.current_window_handle)
        if isinstance(locator_or_element, (WebElement, EventFiringWebElement)):
            self.wait_for_element_clickable(locator_or_element)
            locator_or_element.click()
        else:
            self.wait_for_clickable(locator_or_element).click()

    def type_text(self, locator, text, should_clear=True):
        self.driver.switch_to.window(self.driver.current_window_handle)
        element = self.wait_for_clickable(locator)
        if should_clear:
            element.clear()
        element.send_keys(text)
        return element

    def _waiting_wrapper(self, expectation, locator_or_element, timeout=Config.WAITER_TIMEOUT, raise_on_fail=True):
        self.driver.implicitly_wait(0)
        try:
            if isinstance(expectation, type):
                return WebDriverWait(self.driver, timeout).until(expectation(locator_or_element))
            else:
                return WebDriverWait(self.driver, timeout).until(expectation)
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

    def wait_for_visible(self, locator, timeout=Config.WAITER_TIMEOUT):
        return self._waiting_wrapper(EC.visibility_of_element_located, locator, timeout)

    def wait_for_not_visible(self, locator, timeout=Config.WAITER_TIMEOUT):
        return self._waiting_wrapper(EC.invisibility_of_element_located, locator, timeout)

    def wait_for_clickable(self, locator, timeout=Config.WAITER_TIMEOUT):
        return self._waiting_wrapper(EC.element_to_be_clickable, locator, timeout)

    def wait_for_element_clickable(self, element, timeout=Config.WAITER_TIMEOUT):
        return self._waiting_wrapper(lambda driver: element.is_displayed() and element.is_enabled(), element,
                                     timeout)

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
