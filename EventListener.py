import logging

from selenium.webdriver.support.events import AbstractEventListener

logger = logging.getLogger(__name__)

class BaseListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        logger.error(exception)

    def before_navigate_to(self, url, driver):
        logger.info()