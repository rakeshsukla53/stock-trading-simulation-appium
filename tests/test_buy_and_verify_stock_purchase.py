import unittest
from common import *
from app import *
from prop import *
from mobile.android import *


@on_platforms(android_app)
class BuyAndVerifyStockPurchase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = start_driver(desired_capabilities=self.desired_capabilities,
                                   command_executor=appium_webdriver_host)
        implicitly_wait(self.driver)

    def test_buy_order_history(self):
        driver = self.driver
        SelectCurrencyView.select_us_currency(driver)
        EnterFundAmountView.click_on_continue(driver)
        AccountView()\
            .accept_new_features_modal(driver)\
            .search_and_click_stock(driver)
        shares_count = 10
        order_details_execution = StockView()\
            .wait_for_stock_page_load(driver)\
            .buy_market_order(driver, shares_count)
        print("{} Order details during execution {}".format(generate_formatted_timestamp(), order_details_execution))
        share_value = order_details_execution["share_value"]
        order_details_history = OrderDetailsView.get_order_history_details(driver, share_value)
        print("{} Order details from history page {}".format(generate_formatted_timestamp(), order_details_execution))
        # verify order is properly executed
        self.assertEqual(order_details_history["SYMBOL"], AccountView.apple_ticker_symbol)
        self.assertEqual(order_details_history["ACTION"], "Buy")
        self.assertIn(generate_string_formatted_date(), order_details_history["DATE"])
        self.assertEqual(order_details_history["PRICE"], share_value)
        self.assertEqual(order_details_history["QUANTITY"], shares_count)
        self.assertEqual(order_details_history["TOTAL"], order_details_execution["total_value"])

    def tearDown(self) -> None:
        self.driver.quit()

