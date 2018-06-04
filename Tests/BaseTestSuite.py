import pytest

from TestData.Configuration import Config


@pytest.mark.usefixtures('driver')
class BaseTestSuite(object):
    pass

    def setup(self):
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
        self.driver.maximize_window()