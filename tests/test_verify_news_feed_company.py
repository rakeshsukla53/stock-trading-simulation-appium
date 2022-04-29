import unittest
from mobile.android import *


@on_platforms(android_app)
class VerifyNewsFeedCompany(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = start_driver(desired_capabilities=self.desired_capabilities,
                                   command_executor=appium_webdriver_host)
        implicitly_wait(self.driver)

    def test_verify_news_feed_company(self):
        driver = self.driver
        SelectCurrencyView.select_us_currency(driver)
        EnterFundAmountView.click_on_continue(driver)
        AccountView(driver) \
            .accept_new_features_modal() \
            .search_and_click_stock()
        # scroll to the news feed
        StockView.scroll_to_news_feed(driver)
        list_news_feed_titles = find_elements(driver, StockView.list_of_recent_news_text)
        for el in list_news_feed_titles:
            print("{} News feed titles {}".format(generate_formatted_timestamp(), el.text))
        # click on the first link and verify it's working
        first_element_text = list_news_feed_titles[0].text
        tap(driver, StockView.list_of_recent_news_text, idx=0)
        web_link_locator = ('//android.webkit.WebView[@text="{}"]'.format(first_element_text),
                            "xpath", "{}".format(first_element_text))
        explicit_wait(driver, web_link_locator)
        web_link_title = return_text(driver, web_link_locator)
        self.assertEqual(web_link_title, first_element_text)

    def tearDown(self) -> None:
        self.driver.quit()
