from TestData.Configuration import Config


class wait_for_page_load(object):

    def __init__(self, browser, timeout=Config.WAITER_TIMEOUT):
        self.browser = browser
        self.timeout = timeout

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def __exit__(self, exception_type, exception_value, traceback):
        print(exception_type)
        print(exception_value)
        print(traceback)
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
        return new_page.id != self.old_page.id