import pytest

from TestData.Configuration import Config
from Tests.BaseTestSuite import BaseTestSuite
from PagesFactory import PagesFactory

pytestmark = [pytest.mark.skipif((Config.LOGIN is None or Config.PASSWORD is None), reason='LOGIN and Password required'),
                pytest.mark.login]


class TestLoginSuite(BaseTestSuite):

    def login(self, email, password):
        login_page = PagesFactory(self.driver).main.open_page().toolbox.press_login_button()
        login_page.login(email, password)

    def test_login_logout(self):
        self.login(Config.LOGIN, Config.PASSWORD)
        authorized = PagesFactory(self.driver).find_work_authorized
        assert authorized.is_url_opened()
        login_page = authorized.toolbox.logout()
        assert login_page.is_url_opened()

