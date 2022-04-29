import unittest
from mobile.android import *


@on_platforms(android_app)
class AddandVerifyWatchList(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = start_driver(desired_capabilities=self.desired_capabilities,
                                   command_executor=appium_webdriver_host)
        implicitly_wait(self.driver)

    def test_add_and_verify_watchlist(self):
        driver = self.driver
        SelectCurrencyView.select_us_currency(driver)
        EnterFundAmountView.click_on_continue(driver)
        AccountView(driver) \
            .accept_new_features_modal() \
            .search_and_click_stock()
        StockView(driver)\
            .wait_for_stock_page_load()\
            .add_to_watchlist()
        back(driver)
        watchlist_element = AccountView.get_list_of_watchlist_stocks(driver)
        self.assertIn("AAPL", watchlist_element)
        self.assertIn("Apple Inc.", watchlist_element)

    def tearDown(self) -> None:
        self.driver.quit()

