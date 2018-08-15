import logging

from selenium.webdriver.support.events import AbstractEventListener

from Utils import take_screenshot_with_name

logger = logging.getLogger(__name__)


class BaseListener(AbstractEventListener):

    STEP_PREFIX = "TEST_STEP"
    KNOWN_EXCEPTIONS = []

    def on_exception(self, exception, driver):
        logger.error(exception)
        if exception.msg not in self.KNOWN_EXCEPTIONS:
            take_screenshot_with_name("", driver)
            self.KNOWN_EXCEPTIONS.append(exception.msg)

    def before_navigate_to(self, url, driver):
        logger.info("{} Open {} url".format(self.STEP_PREFIX, url))

    def before_click(self, element, driver):
        logger.info("{} Click on {} element".format(self.STEP_PREFIX, element))