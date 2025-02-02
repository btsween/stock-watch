import yaml
import yfinance as yf

class FinanceUtil:

    def __init__(self):
        with open('./finance/sp500.yml') as f:
            data_map = yaml.safe_load(f)
        self.stock_list = data_map['companies']
        self.buy_list = []

    def find_deals(self):
        for stock in self.stock_list:
            if(self.is_buy(stock)):
                self.buy_list.append("$" + stock)
        return self.buy_list

    def is_buy(self, stock):
        try:
            stock_info = yf.Ticker(stock).info
            moving_200_avg = stock_info['twoHundredDayAverage']
            price = stock_info['bid']
            close_price = stock_info['previousClose']
            if (moving_200_avg is None or price is None or close_price is None):
                return False
            elif (price / moving_200_avg < .9 and price / close_price < .96):
                return True
            else:
                return False
        except:
            print("Failure occured with: ", stock)
            return False

finance_util = FinanceUtil()
