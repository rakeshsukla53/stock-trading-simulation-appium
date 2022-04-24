import unittest
from app import *
from prop import *


@on_platforms(android_app)
class BuyAndVerifyStockPurchase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = start_driver(desired_capabilities=self.desired_capabilities,
                                   command_executor=appium_webdriver_host)
        implicitly_wait(self.driver)

    def test_buy_order_history(self):
        driver = self.driver

    def tearDown(self) -> None:
        self.driver.quit()
