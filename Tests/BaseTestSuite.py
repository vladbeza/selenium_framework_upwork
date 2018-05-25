import pytest

from TestData.Configuration import IMPLICIT_WAIT_TIMEOUT

@pytest.mark.usefixtures('driver')
class BaseTestSuite(object):

    def setup(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_TIMEOUT)
        # self.driver.set_window_size(1920, 1080)