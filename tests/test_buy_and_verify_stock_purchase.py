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
        StockView()\
            .wait_for_stock_page_load(driver)\
            .buy_market_order(driver, shares_count)

    def tearDown(self) -> None:
        self.driver.quit()

