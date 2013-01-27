Ghost Selector
==============

A scrapy selector that supports javascript querying.

How it works
------------

Ghost Selector understands [Selenium](http://seleniumhq.org/)'s [PhantomJS](http://phantomjs.org/) webdriver and takes advantage of the API it offers to behave just like the built-in [Scrapy](http://scrapy.org/) selectors.

Under the hood, selenium uses [GhostDriver](https://github.com/detro/ghostdriver) to talk to PhantomJS via selenium's [WebDriver Wire Protocol](http://code.google.com/p/selenium/wiki/JsonWireProtocol). All Ghost Selector does is wrap whatever selenium returns after running javascript.

Example
-------

	>>> from selenium.webdriver import phantomjs
	>>> from ghostsel import WebdriverXPathSelector
	>>> driver = phantomjs.webdriver.WebDriver()
	>>> driver.get("http://en.wikipedia.org/wiki/Main_Page")
	>>> selector = WebdriverXPathSelector(driver)
	>>> list_items = selector.select_script("return $('#p-navigation li')")
	>>> list_items[0].extract()
	u'Main page'
	>>> 
    

See test for usage.

Credits
-------

Thanks goes to my good friend [Nicolas](http://nicolascadou.com/) for sponsoring its development.