from datetime import datetime


class MarketClosedError(Exception):
    pass


class TradingBot:
    def execute_trade(self):
        pass


class CryptoBot(TradingBot):
    def execute_trade(self):
        print("Crypto Trade Executed")


class StockBot(TradingBot):
    def execute_trade(self):
        hour = datetime.now().hour
        if hour < 9 or hour > 16:
            raise MarketClosedError
        print("Stock Trade Executed")


try:
    bot = StockBot()
    bot.execute_trade()

except MarketClosedError:
    print("Market closed! Trade queued")