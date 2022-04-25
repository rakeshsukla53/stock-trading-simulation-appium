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
    robinhood_ticker_symbol = "HOOD"
    add_the_first_one_now = ("stock.market.simulator.stock.virtual.trading:id/button", "id", "Add The First One Now")
    search_symbol_name_text = (
    "stock.market.simulator.stock.virtual.trading:id/search_editText", "id", "Search for Symbol/Name")
    select_select_symbol = ("stock.market.simulator.stock.virtual.trading:id/tabs", "id", "Select Stock Symbol")
    new_features_got_it = ("android:id/button1", "id", "new features got it")

    def accept_new_features_modal(self, driver):
        if is_element_present(driver, self.new_features_got_it, wait_time=10):
            tap(driver, self.new_features_got_it)
        return self

    def search_and_click_stock(self, driver, stock_ticker_symbol=None):
        if not stock_ticker_symbol:
            stock_ticker_symbol = self.robinhood_ticker_symbol

        explicit_wait(driver, self.search_symbol_name_text)
        input_text(driver, self.search_symbol_name_text, stock_ticker_symbol)
        tap(driver, self.select_select_symbol)
        return self


class StockView:
    select_one_month = ("stock.market.simulator.stock.virtual.trading:id/Time_1M", "id", "First One Month")
    stock_buy_button = ("stock.market.simulator.stock.virtual.trading:id/btnBuy", "id", "Button Buy")
    select_market_buy = ('//*[@id="android:id/select_dialog_listview"]/android.widget.TextView[@text="Market Buy"]',
                         "xpath", "Market Buy Order")
    shares_input = (
    '//*[@id="stock.market.simulator.stock.virtual.trading:id/tabs"]/android.widget.TextView[@text="ORDER HISTORY"]',
    "xpath", "Input Order")
    place_order = ("stock.market.simulator.stock.virtual.trading:id/button", "id", "Place Order")
