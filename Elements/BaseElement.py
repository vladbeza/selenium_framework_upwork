from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BaseElement(object):

    def __init__(self, locator):
        self.locator = locator
        self.driver = None

    def __get__(self, obj, owner):
        self.driver = obj.driver
        return self.locator

    def get_element(self):
        return self.driver.find_element(*self.locator)

    def is_exist(self):
        self.driver.implicitly_wait(1)
        try:
            element = self.driver.find_element(*self.locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(10)


    def wait_for(self, condition, is_positive=True, timeout=3):
        wait = WebDriverWait(self.driver, timeout)
        if is_positive:
            wait.until(condition(self.locator))
        else:
            wait.until_not(condition(self.locator))

    def scroll_to_element(self):
        element = self.driver.find_element(*self.locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return element
