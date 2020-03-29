import yaml

class FinanceUtil:

    def __init__(self):
        with open('./finance/stocks_list.yml') as f:
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
        print(stock)
        return True

finance_util = FinanceUtil()
