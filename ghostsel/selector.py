from scrapy.selector import XPathSelector, XPathSelectorList


class WebdriverXPathSelector(XPathSelector):
    """
    Scrapy selector that knows how to run javascript in remote
    browser through GhostDriver > PhantomJs.
    """

    def __init__(self, driver, element=None, *args, **kwargs):
        """ Override __init__ and add `driver` and `element` args. """
        # keep track of webdriver/selenium related attributes
        self.driver = driver
        self.element = element
        super(WebdriverXPathSelector, self).__init__(*args, **kwargs)

    def _cleanup_result(self, result):
        if type(result) is not list:
            result = [result]
        return [self.__class__(driver=self.driver, element=e) for e in result]

    def select(self, xpath):
        """
        Override of select method which uses selenium's
        `find_elements_by_xpath` method.
        """
        xpathev = self.element if self.element else self.driver
        result = self._cleanup_result(xpathev.find_elements_by_xpath(xpath))
        return XPathSelectorList(result)

    def select_script(self, script, *args):
        """ Return elements based on passed js script selector. """
        result = self._cleanup_result(self.driver.execute_script(script, *args))
        return XPathSelectorList(result)

    def extract(self):
        """ Extract text from selenium element. """
        return self.element.text if self.element else None
