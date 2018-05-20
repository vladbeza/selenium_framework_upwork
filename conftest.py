import pytest
import logging
from selenium import webdriver
from TestData import Configuration
from selenium.common.exceptions import WebDriverException

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
                params=Configuration.BROWSERS)
def driver(request):
    try:
        driver = BROWSERS[request.param.upper()]()
        request.cls.driver = driver
        yield
    except (WebDriverException, Exception) as e:
        logging.warning("Unsupported browser type {}".format(e))
    else:
        driver.quit()
