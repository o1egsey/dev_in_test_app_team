from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_element_by_type(self, method, value):
        if method == 'id':
            return self.driver.find_element_by_id(value)
        elif method == 'name':
            return self.driver.find_element_by_name(value)
        elif method == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif method == 'class':
            return self.driver.find_element_by_class(value)
        else:
            raise Exception('Invalid method provided')

    def get_element(self, locator):
        """
        Returns element based on provided locator.

        Locator include the method and locator value in a tuple like ('id', 'value').
        :param locator:
        :return:
        """

        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_element_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_element_by_type(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def wait_visible(self, locator, timeout=25):
        """Wait until element is visible. If not - throw exception"""
        i = 0
        while i != timeout:
            try:
                self.is_visible(locator)
                return self.get_element(locator)
            except NoSuchElementException:
                sleep(1)
                i += 1
        raise Exception('Element never became visible: %s (%s)' % (locator[0], locator[1]))

    def click(self, locator):
        element = self.wait_visible(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.wait_visible(locator)
        element.send_keys(text)
        sleep(0.5)

    def is_visible(self, locator):
        try:
            self.get_element(locator).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def get_text(self, locator):
        """Getting text from element"""
        element = self.wait_visible(locator)
        return element.text
