import random
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
    watchlist_tab_line = ('//android.widget.TextView[@text="Watchlist"]', "xpath", "WatchList")
    list_of_watchlist_stocks = ('//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/constraintLayout2"]'
                                '/android.widget.TextView', "xpath", "List of Watchlist Stocks")

    def __init__(self, driver):
        self.driver = driver

    def accept_new_features_modal(self):
        if is_element_present(self.driver, self.new_features_got_it, wait_time=10):
            tap(self.driver, self.new_features_got_it)
        return self

    def search_and_click_stock(self, stock_ticker_symbol=None):
        if not stock_ticker_symbol:
            stock_ticker_symbol = self.apple_ticker_symbol
        explicit_wait(self.driver, self.search_symbol_name_text)
        input_text(self.driver, self.search_symbol_name_text, stock_ticker_symbol)
        tap(self.driver, self.search_symbol_name_text)
        explicit_wait(self.driver, self.apple_stock_tab)
        tap(self.driver, self.apple_stock_tab)
        return self

    @classmethod
    def get_list_of_watchlist_stocks(cls, driver):
        explicit_wait(driver, AccountView.watchlist_tab_line)
        el = find_elements(driver, AccountView.list_of_watchlist_stocks)
        return map(lambda x: x.text, el)


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
    def get_order_history_details(cls, driver, share_value):
        # make sure you are in the account view page
        explicit_wait(driver, OrderDetailsView.order_history_tab)
        tap(driver, OrderDetailsView.order_history_tab)
        share_value_locator = ('//android.widget.TextView[@text="${}"]'.format(share_value), "xpath",
                               "Share Price {} Link".format(share_value))
        explicit_wait(driver, share_value_locator)
        tap(driver, share_value_locator)
        # create order details object
        order_details = {}
        list_order_details_keys = map(lambda x: x.text, find_elements(driver, OrderDetailsView.order_details_keys))
        list_order_details_values = map(lambda x: x.text, find_elements(driver, OrderDetailsView.order_details_values))
        for key, value in zip(list_order_details_keys, list_order_details_values):
            order_details[key] = value

        return order_details


class StockView:
    select_one_month = ("stock.market.simulator.stock.virtual.trading:id/Time_1M", "id", "First One Month")
    one_month_ago_text = (
    '//android.widget.TextView[@resource-id="stock.market.simulator.stock.virtual.trading:id/tvTime" '
    'and @text="1M AGO"]', "xpath", "One Month Ago Text")
    date_text = ('//android.widget.TextView[@resource-id="stock.market.simulator.stock.virtual.trading:id/tvTime"]',
                 "xpath", "Date Text")
    stock_buy_button = ("stock.market.simulator.stock.virtual.trading:id/btnBuy", "id", "Button Buy")
    select_market_buy = ('//*[@resource-id="android:id/text1" and @text="  Market Buy"]', "xpath", "Market Buy Order")
    shares_input = ('//android.widget.EditText[@resource-id="stock.market.simulator.stock.virtual.trading:id/tvShare"]',
                    "xpath", "Input Order")
    share_value = ('//android.widget.TextView[@resource-id="stock.market.simulator.stock.virtual.trading:id/tvPrice"]',
                   "xpath", "Shares Price")
    total_share_price = (
    '//android.widget.EditText[@resource-id="stock.market.simulator.stock.virtual.trading:id/tvTotal"]',
    "xpath", "Total Value")
    place_order = (
    '//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/btnPlaceOrder" and @text="PLACE ORDER"]',
    "xpath", "Place Order")
    watchlist_star_icon = (
    "stock.market.simulator.stock.virtual.trading:id/action_favorite", "id", "Watchlist Star Icon")
    recent_news_text = ('//android.widget.TextView[@text="Recent News"]', "xpath", "Recent News Text")
    list_of_recent_news_text = ('//*[@resource-id="stock.market.simulator.stock.virtual.trading:id/linearLayout6"]/'
                                'android.widget.TextView[@resource-id="stock.market.'
                                'simulator.stock.virtual.trading:id/textView14"]', "xpath", "News Topic")

    def __init__(self, driver):
        self.driver = driver

    def buy_market_order(self, shares_count):
        tap(self.driver, self.stock_buy_button)
        explicit_wait(self.driver, self.select_market_buy)
        tap(self.driver, self.select_market_buy)
        explicit_wait(self.driver, self.shares_input)
        input_text(self.driver, self.shares_input, shares_count * 10)
        share_value = return_text(self.driver, self.share_value)
        total_value = return_text(self.driver, self.total_share_price)
        tap(self.driver, self.place_order)

        order_details = {
            "share_value": share_value,
            "total_value": total_value
        }

        return order_details

    def add_to_watchlist(self):
        explicit_wait(self.driver, self.watchlist_star_icon)
        tap(self.driver, self.watchlist_star_icon)
        return self

    def verify_one_month_chart_loads(self):
        explicit_wait(self.driver, self.select_one_month)
        tap(self.driver, self.select_one_month)
        explicit_wait(self.driver, self.one_month_ago_text)
        return self

    def get_price_date_info_by_random_press(self):
        """ Long press by coordinate and move along the graph. """
        action = TouchAction(self.driver)
        x = random.randint(600, 800)
        # this set of x and y coordinates will only on Pixel 2 and similar mobile phones
        action.long_press(x=400, y=1000).wait(2000).move_to(x=x, y=1000).perform()
        print("{} date information {}".format(generate_formatted_timestamp(),
                                              return_text(self.driver, self.date_text)))
        print("{} price information {}".format(generate_formatted_timestamp(),
                                               return_text(self.driver, self.share_value)))
        action.long_press(x=400, y=1000).wait(2000).move_to(x=x, y=1000).release().perform()
        return self

    def wait_for_stock_page_load(self):
        explicit_wait(self.driver, self.stock_buy_button)
        explicit_wait(self.driver, self.select_one_month)
        return self

    @classmethod
    def scroll_to_news_feed(cls, driver):
        # try few times to scroll to the news feed section
        count = 0
        end_y = -400
        while count <= 5:
            sleep(3)
            # the swipe coordinates will only work for Pixel 2 and similar device sizes
            swipe(driver, (150, 400, 150, end_y))
            element_news_section = find_element(driver, StockView.recent_news_text)
            element_news_title = find_element(driver, StockView.list_of_recent_news_text)
            if element_news_title and element_news_section:
                print("{} Scrolling to Recent News".format(generate_formatted_timestamp()))
                return
            count += 1
            end_y = -100
        raise "Recent News Text is not found"
