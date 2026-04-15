from datetime import datetime


class MarketClosedError(Exception):
    pass


class TradingBot:
    def execute_trade(self):
        pass


class CryptoBot(TradingBot):
    def execute_trade(self):
        print("CryptoBot: Trade executed (24/7 market)")


class StockBot(TradingBot):
    def execute_trade(self):
        try:
            hour = datetime.now().hour

            if hour < 9 or hour > 16:
                raise MarketClosedError

            print("StockBot: Trade executed")
        except MarketClosedError:
            print("StockBot: Market closed, trade queued")


bots = [CryptoBot(), StockBot()]

for bot in bots:
    bot.execute_trade()