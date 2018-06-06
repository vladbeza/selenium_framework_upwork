import pytest

from TestData.Configuration import Config


@pytest.mark.usefixtures('driver')
class BaseTestSuite(object):
    pass

    def setup(self):
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
        if self.driver.name.upper() != "CHROME":
            self.driver.maximize_window()
