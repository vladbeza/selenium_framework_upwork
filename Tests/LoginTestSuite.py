import pytest

from Tests.BaseTestSuite import BaseTestSuite
from TestData.Configuration import Config
from Pages.MainPage import MainPage
from Pages.LoginPage import LoginPage
from Pages.FindWorkPageAuthorized import FindWorkPageAuthorized
from Pages.LoginPage import LoginPage

from Utils import wait_for_page_load


pytestmark = [pytest.mark.skipif((Config.LOGIN is None or Config.PASSWORD is None), reason='LOGIN and Password required'),
                pytest.mark.login]


class TestLoginSuite(BaseTestSuite):

    def login(self, email, password):
        main_page = MainPage(self.driver)
        main_page.open_page()
        main_page.toolbox.press_login_button()
        login_page = LoginPage(self.driver)
        with wait_for_page_load(self.driver):
            login_page.login(email, password)

    def test_login(self):
        self.login(Config.LOGIN, Config.PASSWORD)
        assert self.driver.current_url == FindWorkPageAuthorized(self.driver).get_url()

    def test_logout(self):
        # self.login(Config.LOGIN, Config.PASSWORD)
        FindWorkPageAuthorized(self.driver).toolbox.logout()
        assert self.driver.current_url == LoginPage(self.driver).get_url()

