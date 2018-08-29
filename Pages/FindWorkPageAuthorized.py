from Elements.AuthorizedToolbox import AuthorizedToolbox
from Pages.BasePage import BasePage


class FindWorkPageLocators(object):

    pass


class FindWorkPageAuthorized(BasePage):

    URL = "/ab/find-work/"

    def __init__(self, driver):
        super(FindWorkPageAuthorized, self).__init__(driver)
        self.toolbox = AuthorizedToolbox(driver)
