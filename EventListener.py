from selenium.webdriver.support.events import AbstractEventListener


class BaseListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        # create_screenshot_on_failure(driver)
        pass