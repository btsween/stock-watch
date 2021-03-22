import yaml
import yfinance as yf

class FinanceUtil:

    def __init__(self):
        with open('./finance/sp500.yml') as f:
            data_map = yaml.safe_load(f)
            #self.stocks_list = data_map.
        self.stock_list = data_map['companies']
        self.buy_list = []

    def find_deals(self):
        for stock in self.stock_list:
            if(self.is_buy(stock)):
                self.buy_list.append(stock)
        return self.buy_list

    def is_buy(self, stock):
        print("trying for " + stock)
        try:
            stock_info = yf.Ticker(stock).info
            moving_200_avg = stock_info['twoHundredDayAverage']
            price = stock_info['bid']
            close_price = stock_info['previousClose']
            if(moving_200_avg is None or price is None or close_price is None):
                return False
            elif(price / moving_200_avg < .6 and price / close_price < .96):
                return True
            else:
                return False
        except:
            print("d'oh didnt work")
            return False

    # def is_buy(self, stock):
    #     print("trying for " + stock)
    #     stock_info = yf.Ticker(stock).info
    #     moving_200_avg = stock_info['twoHundredDayAverage']
    #     price = stock_info['bid']
    #     close_price = stock_info['previousClose']
    #     if(moving_200_avg is None or price is None or close_price is None):
    #         return False
    #     elif(price / moving_200_avg < .5 and price / close_price < .9):
    #         return True
    #     else:
    #         return False
    #     print("d'oh didnt work")
    #     return False
finance_util = FinanceUtil()
