from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Toolboxes.AuthorizedToolbox import AuthorizedToolbox


class FindWorkPageLocators(object):

    pass


class FindWorkPageAuthorized(BasePage):

    URL = "/ab/find-work/"

    def __init__(self, driver):
        super(FindWorkPageAuthorized, self).__init__(driver)
        self.toolbox = AuthorizedToolbox(driver)