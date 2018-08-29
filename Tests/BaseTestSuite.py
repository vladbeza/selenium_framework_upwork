import pytest

from Utils import CatchAssertions


@pytest.mark.usefixtures('driver')
class BaseTestSuite(object, metaclass=CatchAssertions):
    pass
