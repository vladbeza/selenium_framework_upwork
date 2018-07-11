import pytest
import os
import logging
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://www.upwork.com", help="Base url")
    parser.addoption("--browser", action="append")
    parser.addoption("--login", action="store", required=False)
    parser.addoption("--password", action="store", required=False)
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
    parser.addoption('--remote_hub',
                     action='store',
                     help='remote hub address')
    parser.addoption('--platform',
                     action='store',
                     help='platform where run remote test')


def pytest_configure(config):
    Config.BASE_URL = config.getoption("--base_url")
    Config.LOGIN = get_optional_arg(config, "--login")
    Config.PASSWORD = get_optional_arg(config, "--password")
    Config.REMOTE_HUB = get_optional_arg(config, "--remote_hub")
    Config.PLATFORM = get_optional_arg(config, "--platform")
    browsers = get_optional_arg(config, "--browser")
    if browsers is not None:
        Config.BROWSERS = browsers


def get_optional_arg(config, option):
    try:
        return config.getoption(option)
    except ValueError as a:
        logger.warning("Couldn't get option {}. {}".format(option, a))
        return None


def pytest_generate_tests(metafunc):
    if 'driver' in metafunc.fixturenames:
        metafunc.parametrize("driver", Config.BROWSERS, indirect=True, scope="class")


def get_driver_for_browser(request, browser):
    if browser == "CHROME":
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-popup-blocking")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("useAutomationExtension", False)
        chrome_profile = get_optional_arg(request.config, "--chrome_profile_path")
        if chrome_profile is not None:
            options.add_argument("user-data-dir={}".format(chrome_profile))
        if Config.REMOTE_HUB is not None:
            return BROWSERS["REMOTE"](command_executor=Config.REMOTE_HUB, desired_capabilities=DesiredCapabilities.CHROME,
                                      options=options)
        chromedriver_path = get_optional_arg(request.config, "--chromedriver_path")
        return BROWSERS[browser](executable_path=chromedriver_path if chromedriver_path is not None else "chromedriver",
                                 chrome_options=options)
    if Config.REMOTE_HUB is not None:
        capabilities = None
        if browser == "FIREFOX":
            capabilities = DesiredCapabilities.FIREFOX
        elif browser == "IE":
            capabilities = DesiredCapabilities.INTERNETEXPLORER
        elif browser == "SAFARI":
            capabilities = DesiredCapabilities.SAFARI

        if Config.PLATFORM is not None:
            capabilities["platform"] = Config.PLATFORM

        return BROWSERS["REMOTE"](command_executor=Config.REMOTE_HUB,
                                  desired_capabilities=capabilities)

    if browser == "FIREFOX":
        geckodriver_path = get_optional_arg(request.config, "--geckodriver_path")
        return BROWSERS[browser](executable_path=geckodriver_path if geckodriver_path is not None else "geckodriver")

    return BROWSERS[browser]()


@pytest.fixture
def driver(request):
    driver = None
    try:
        browser_name = request.param.upper()
        driver = get_driver_for_browser(request, browser_name)
        logger.info(driver.capabilities)
        driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
        driver.set_page_load_timeout(60)
        if driver.name.upper() != "CHROME":
            driver.maximize_window()
        if request.cls is not None:
            request.cls.driver = driver
        yield driver
    except (WebDriverException, Exception) as e:
        logging.fatal(str(e))
        raise e
    finally:
        if driver is not None:
            driver.quit()


@pytest.fixture(scope="function", autouse=True)
def create_screenshot_on_failure(request):
    yield
    test_name = request.node.name
    if request.node.rep_call.failed:
        try:
            current_date = str(datetime.now()).split(".")[0]
            for symbol in [" ", "[", "]", ".", ":"]:
                current_date = current_date.replace(symbol, "_")
                test_name = test_name.replace(symbol, "_")
            screens_folder = os.path.join(os.getcwd(), "Screenshots")
            if not os.path.exists(screens_folder):
                os.makedirs(screens_folder)
            screen_path = os.path.join(screens_folder, "{}{}.png".format(test_name, current_date))
            request.instance.driver.save_screenshot(screen_path)
        except Exception as ex:
            logger.warning("Couldn't take screenshot. {}".format(ex))


def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" %previousfailed.name)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    if "login" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

