import pytest
import logging
import os
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from TestData import Configuration
from TestData.Configuration import IMPLICIT_WAIT_TIMEOUT

BROWSERS = {
    'FIREFOX': webdriver.Firefox,
    'CHROME': webdriver.Chrome,
    'SAFARI': webdriver.Safari,
    'OPERA': webdriver.Opera,
    'IE': webdriver.Ie,
    'PHANTOMJS': webdriver.PhantomJS,
    'REMOTE': webdriver.Remote
}


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://www.upwork.com/", help="Base url")
    parser.addoption("--browser", action="append", default=["Firefox"])
    parser.addoption('--host',
                     help='host that the selenium server is listening on, '
                          'which will default to the cloud provider default '
                          'or localhost.')
    parser.addoption('--port', type=int,
                     help='port that the selenium server is listening on, '
                          'which will default to the cloud provider default '
                          'or localhost.')


def pytest_configure(config):
    Configuration.BASE_URL = config.getoption("--base_url")
    Configuration.BROWSERS = config.getoption("--browser")


@pytest.fixture(scope="class",
                params=Configuration.BROWSERS,
                autouse=True)
def driver(request):
    try:
        driver = BROWSERS[request.param.upper()]()
        driver.implicitly_wait(IMPLICIT_WAIT_TIMEOUT)
        driver.maximize_window()
        request.cls.driver = driver
        yield
    except (WebDriverException, Exception) as e:
        logging.warning("Unsupported browser type {}".format(e))
    else:
        driver.quit()


@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield
    test_name = request.node.name
    if request.node.rep_call.failed:
        current_date = str(datetime.now()).split(".")[0]
        for symbol in [" ", "[", "]", ".", ":"]:
            current_date = current_date.replace(symbol, "_")
            test_name = test_name.replace(symbol, "_")
        screen_path = os.path.join(os.getcwd(), "Screenshots", "{}{}.png".format(test_name, current_date))
        print(screen_path)
        print(request.cls.driver.save_screenshot(screen_path))


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
