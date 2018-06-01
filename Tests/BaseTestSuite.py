import pytest
import os
from datetime import datetime

from TestData.Configuration import IMPLICIT_WAIT_TIMEOUT


@pytest.mark.usefixtures('driver')
class BaseTestSuite(object):
    pass

    def setup(self):
        self.driver.implicitly_wait(IMPLICIT_WAIT_TIMEOUT)
        self.driver.maximize_window()