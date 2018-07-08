import pytest

from TestData.Configuration import Config


@pytest.mark.usefixtures('driver')
class BaseTestSuite(object):
    pass
