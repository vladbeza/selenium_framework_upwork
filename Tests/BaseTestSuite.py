import pytest
import os
from datetime import datetime

from TestData.Configuration import IMPLICIT_WAIT_TIMEOUT


@pytest.mark.usefixtures('driver')
class BaseTestSuite(object):
    pass

    # def setup(self):
    #     self.driver.implicitly_wait(IMPLICIT_WAIT_TIMEOUT)
    #     self.driver.maximize_window()
    #
    # def teardown(self, request):
    #     print("tear_down")
    #     test_name = request.node.name
    #     if request.node.rep_call.failed:
    #         current_date = str(datetime.now()).replace(" ", "_")
    #         screen_path = os.path.join("Screenshots", "{}{}.png".format(test_name, current_date))
    #         self.driver.save_screenshot(screen_path)
