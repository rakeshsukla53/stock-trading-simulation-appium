from app import *


class SelectCurrencyView:
    usd_dollar = (
    '//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/recyclerView"]/android.widget.Button[@index="0"]',
    'xpath', 'US Dollar')

    @classmethod
    def select_us_currency(cls, driver):
        explicit_wait(driver, SelectCurrencyView.usd_dollar)
        tap(driver, SelectCurrencyView.usd_dollar)


class EnterFundAmountView:
    continue_button = ("stock.market.simulator.stock.virtual.trading:id/btnContinue", "id", "Continue Button")

    @classmethod
    def click_on_continue(cls, driver):
        tap(driver, EnterFundAmountView.continue_button)


class AccountView:
    apple_ticker_symbol = "AAPL"
    add_the_first_one_now = ("stock.market.simulator.stock.virtual.trading:id/button", "id", "Add The First One Now")
    search_symbol_name_text = (
    "stock.market.simulator.stock.virtual.trading:id/search_editText", "id", "Search for Symbol/Name")
    select_select_symbol = ("stock.market.simulator.stock.virtual.trading:id/tabs", "id", "Select Stock Symbol")
    new_features_got_it = ("android:id/button1", "id", "new features got it")
    apple_stock_tab = ('//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/textView" '
                           'and @text="AAPL Apple Inc."]', "xpath", "Robinhood Markets")

    def accept_new_features_modal(self, driver):
        if is_element_present(driver, self.new_features_got_it, wait_time=10):
            tap(driver, self.new_features_got_it)
        return self

    def search_and_click_stock(self, driver, stock_ticker_symbol=None):
        if not stock_ticker_symbol:
            stock_ticker_symbol = self.apple_ticker_symbol
        explicit_wait(driver, self.search_symbol_name_text)
        input_text(driver, self.search_symbol_name_text, stock_ticker_symbol)
        tap(driver, self.search_symbol_name_text)
        explicit_wait(driver, self.apple_stock_tab)
        tap(driver, self.apple_stock_tab)
        return self


class OrderDetailsView:
    order_history_tab = ('//android.widget.TextView[@text="ORDER HISTORY"]', "xpath", "Order History")
    shares_count = ("stock.market.simulator.stock.virtual.trading:id/tvShare", "id", "Shares Count")
    share_value = ("stock.market.simulator.stock.virtual.trading:id/tvShareValue", "id", "Shares Value")
    shares_total_value = ("stock.market.simulator.stock.virtual.trading:id/tvTotal", "id", "Shares Total Value")
    buy_order_locator_order = ("stock.market.simulator.stock.virtual.trading:id/textView6", "id", "BUY HOOD")
    buy_order_text_link = ("stock.market.simulator.stock.virtual.trading:id/textView7", "id", "Buy Order Link")
    order_details = ('//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/linearLayout4"]', "xpath",
                     "Order Details")
    order_details_keys = ('//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/textView8"]', "xpath",
                          "Order Details Key")
    order_details_values = ('//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/textView9"]', "xpath",
                            "Order Details Value")

    @classmethod
    def get_order_history_details(cls, driver,  share_value):
        # make sure you are in the account view page
        explicit_wait(driver, OrderDetailsView.order_history_tab)
        share_value_locator = ('//android.widget.TextView[@text="${}"]'.format(share_value), "xpath",
                               "Share Price {} Link".format(share_value))
        explicit_wait(driver, share_value_locator)
        tap(driver, share_value_locator)
        # create order details object
        order_details = {}
        list_order_details_keys = find_elements(driver, OrderDetailsView.order_details_keys)
        list_order_details_values = find_elements(driver, OrderDetailsView.order_details_values)
        for key, value in zip(list_order_details_keys, list_order_details_values):
            order_details[key] = value

        return order_details


class StockView:
    select_one_month = ("stock.market.simulator.stock.virtual.trading:id/Time_1M", "id", "First One Month")
    stock_buy_button = ("stock.market.simulator.stock.virtual.trading:id/btnBuy", "id", "Button Buy")
    select_market_buy = ('//*[@resource-id="android:id/text1" and @text="  Market Buy"]', "xpath", "Market Buy Order")
    shares_input = ('//android.widget.EditText[@resource-id="stock.market.simulator.stock.virtual.trading:id/tvShare"]',
                    "xpath", "Input Order")
    share_value = ('//android.widget.TextView[@resource-id="stock.market.simulator.stock.virtual.trading:id/tvPrice"]',
                   "xpath", "Shares Price")
    total_share_price =('//android.widget.EditText[@resource-id="stock.market.simulator.stock.virtual.trading:id/tvTotal"]',
                        "xpath", "Total Value")
    place_order = ('//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/btnPlaceOrder" and @text="PLACE ORDER"]',
                   "xpath", "Place Order")

    def buy_market_order(self, driver, shares_count):
        tap(driver, self.stock_buy_button)
        explicit_wait(driver, self.select_market_buy)
        tap(driver, self.select_market_buy)
        explicit_wait(driver, self.shares_input)
        input_text(driver, self.shares_input, shares_count*10)
        share_value = return_text(driver, self.share_value)
        total_value = return_text(driver, self.total_share_price)
        tap(driver, self.place_order)

        order_details = {
            "share_price": share_value,
            "total_value": total_value
        }

        return order_details

    def wait_for_stock_page_load(self, driver):
        explicit_wait(driver, self.stock_buy_button)
        explicit_wait(driver, self.select_one_month)
        return self
