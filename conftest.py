import pytest
import logging
import os
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
    parser.addoption('--firefox_profile_path',
                     action="store",
                     help='path to Firefox browser specific profile')
    parser.addoption('--geckodriver_path',
                     action="store",
                     help='path to Firefox driver executable')
    parser.addoption('--chrome_profile_path',
                     action="store",
                     help='path to Chrome browser specific profile')
    parser.addoption('--chromedriver_path',
                     action="store",
                     help='path to Chrome driver executable')


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


def get_driver_for_browser(browser):
    if browser == "CHROME":
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-popup-blocking")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.accept_untrusted_certs = True
        options.add_argument("--no-sandbox")
        options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data")
        return BROWSERS[browser](chrome_options=options)
        # capabilities = {
        #                 'browserName': 'chrome',
        #                 'chromeOptions':  {
        #                 'useAutomationExtension': False,
        #                 'forceDevToolsScreenshot': True,
        #                 'args': ['--start-maximized', '--disable-infobars']
        #                     }
        #                 }
        # return BROWSERS[browser](desired_capabilities=capabilities)
    else:
        return BROWSERS[browser]()


@pytest.fixture(scope="class")
def driver(request):
    try:
        browser_name = request.param.upper()
        driver = get_driver_for_browser(browser_name)
        print(driver.capabilities)
        request.cls.driver = driver
        yield
    except (WebDriverException, Exception) as e:
        logging.fatal("Unsupported browser type {}".format(e))
        raise e
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
        screens_folder = os.path.join(os.getcwd(), "Screenshots")
        if not os.path.exists(screens_folder):
            os.makedirs(screens_folder)
        screen_path = os.path.join(screens_folder, "{}{}.png".format(test_name, current_date))
        request.cls.driver.save_screenshot(screen_path)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

