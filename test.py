import unittest
from selenium.webdriver import phantomjs

from scrapy.contrib.loader import XPathItemLoader
from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join
from scrapy.utils.markup import remove_entities

from ghostsel import WebdriverXPathSelector


class NavItem(Item):
    name = Field(input_processor=MapCompose(remove_entities),
                 output_processor=Join())


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.driver = phantomjs.webdriver.WebDriver()
        self.driver.get("http://en.wikipedia.org/wiki/Main_Page")
        self.selector = WebdriverXPathSelector(self.driver)

    def test_wikipedia_links(self):
        navs = self.selector.select_script("return $('#p-navigation li')")
        nav_items = []
        for nav in navs:
            loader = XPathItemLoader(NavItem(), nav)
            loader.add_xpath('name', './/a')
            nav_items.append(loader.load_item())

        expected = [u'Main page', u'Contents', u'Featured content',
                    u'Current events', u'Random article', u'Donate to Wikipedia']

        for i, item in enumerate(nav_items):
            self.assertEqual(item['name'], expected[i])


if __name__ == '__main__':
    unittest.main()
