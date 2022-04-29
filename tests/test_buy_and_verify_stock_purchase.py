import unittest
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
        AccountView(driver) \
            .accept_new_features_modal() \
            .search_and_click_stock()
        shares_count = 10
        order_details_execution = StockView(driver) \
            .wait_for_stock_page_load() \
            .verify_one_month_chart_loads() \
            .get_price_date_info_by_random_press() \
            .buy_market_order(shares_count)
        print("{} Order details during execution {}".format(generate_formatted_timestamp(), order_details_execution))
        share_value = order_details_execution["share_value"]
        order_details_history = OrderDetailsView.get_order_history_details(driver, share_value)
        print("{} Order details from history page {}".format(generate_formatted_timestamp(), order_details_execution))
        # verify order is properly executed
        formatted_share_price = round(float(order_details_history["PRICE"]), 2)
        share_value = round(float(share_value), 2)
        self.assertEqual(order_details_history["SYMBOL"], AccountView.apple_ticker_symbol)
        self.assertEqual(order_details_history["ACTION"], "Buy")
        self.assertIn(generate_string_formatted_date(), order_details_history["DATE"])
        self.assertEqual(formatted_share_price, share_value)
        self.assertEqual(int(order_details_history["QUANTITY"]), int(shares_count))
        self.assertEqual(order_details_history["TOTAL"], order_details_execution["total_value"])

    def tearDown(self) -> None:
        self.driver.quit()
