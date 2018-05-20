from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Toolboxes.MainToolbox import MainToolbox
from Elements.BaseElement import BaseElement


class MainPageLocators(object):




class MainPage(BasePage):

    URL = ""

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.toolbox = MainToolbox(driver)

