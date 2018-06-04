import pytest
import logging
import os
import sys
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from TestData.Configuration import Config

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
    parser.addoption("--base_url", action="store", default="https://www.upwork.com", help="Base url")
    parser.addoption("--browser", action="append")
    parser.addoption("--login", action="store", required=False)
    parser.addoption("--password", action="store", required=False)
    parser.addoption('--host',
                     action="store",
                     required=False,
                     help='host that the selenium server is listening on, '
                          'which will default to the cloud provider default '
                          'or localhost.')
    parser.addoption('--port', type=int, action="store",
                     required=False,
                     help='port that the selenium server is listening on, '
                          'which will default to the cloud provider default '
                          'or localhost.')


def pytest_configure(config):
    Config.BASE_URL = config.getoption("--base_url")
    Config.LOGIN = get_optional_arg(config, "--login")
    Config.PASSWORD = get_optional_arg(config, "--password")
    browsers = get_optional_arg(config, "--browser")
    if browsers is not None:
        Config.BROWSERS = browsers


def get_optional_arg(config, option):
    try:
        return config.getoption(option)
    except ValueError as a:
        print("Couldn't get option {}. {}".format(option, a))
        return None


def pytest_generate_tests(metafunc):
    if 'driver' in metafunc.fixturenames:
        metafunc.parametrize("driver", Config.BROWSERS, indirect=True, scope="class")


def get_capabilities(browser):
    capabilities = {}
    if browser == "CHROME":
        capabilities["acceptInsecureCerts"] = True
    return capabilities

@pytest.fixture(scope="class")
def driver(request):
    try:
        c = "--allow-running-insecure-content"
        capabilities = get_capabilities(request.param.upper())
        driver = BROWSERS[request.param.upper()](desired_capabilities=capabilities)
        print(driver.capabilities)
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
        request.cls.driver.save_screenshot(screen_path)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
