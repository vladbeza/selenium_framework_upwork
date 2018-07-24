import os
import allure
import logging
import functools

from datetime import datetime

from TestData.Configuration import Config


def take_screenshot_with_name(name, driver):
    try:
        current_date = str(datetime.now()).split(".")[0]
        for symbol in [" ", "[", "]", ".", ":"]:
            current_date = current_date.replace(symbol, "_")
            name = name.replace(symbol, "_")
        screens_folder = os.path.join(os.path.dirname(os.getcwd()), "Screenshots")
        if not os.path.exists(screens_folder):
            os.makedirs(screens_folder)
        screen_path = os.path.join(screens_folder, "{}{}.png".format(name, current_date))
        driver.save_screenshot(screen_path)
        allure.attach.file(screen_path, attachment_type=allure.attachment_type.PNG)
    except Exception as ex:
        logging.warning("Couldn't take screenshot. {}".format(ex))


def take_screenshot_on_assertion(test_method):

    @functools.wraps(test_method)
    def test_decorator(self, *args, **kwars):
        try:
            test_method(self, *args, **kwars)
        except AssertionError as assertion:
            take_screenshot_with_name(test_method.__name__, self.driver)
            raise assertion

    return test_decorator


class CatchAssertions(type):

    def __new__(cls, clsname, superclasses, attributesdict):
        for attr_name, attr in attributesdict.items():
            if callable(attr) and attr_name.startswith("test"):
                attributesdict[attr_name] = take_screenshot_on_assertion(attr)
        return type.__new__(cls, clsname, superclasses, attributesdict)


class wait_for_page_load(object):

    def __init__(self, browser, timeout=Config.WAITER_TIMEOUT):
        self.browser = browser
        self.timeout = timeout

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')
        self.old_url = self.browser.current_url

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type:
            raise exception_type
        self.wait_for()

    def wait_for(self):
        import time

        start_time = time.time()
        while time.time() < start_time + self.timeout:
            if self.page_has_loaded():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Timeout waiting for Page loading'
        )

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        new_url = self.browser.current_url
        return new_page.id != self.old_page.id and new_url != self.old_url
