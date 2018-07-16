import logging

from selenium.webdriver.support.events import AbstractEventListener

logger = logging.getLogger(__name__)


class BaseListener(AbstractEventListener):

    STEP_PREFIX = "TEST_STEP"

    # def on_exception(self, exception, driver):
    #     logger.error(exception)

    def before_navigate_to(self, url, driver):
        logger.info("{} Open {} url".format(self.STEP_PREFIX, url))

    def before_click(self, element, driver):
        logger.info("{} Click on {} element".format(self.STEP_PREFIX, element))