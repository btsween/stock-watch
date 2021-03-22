from finance.finance_util import finance_util
from messaging.text_util import text_util

deal_list = finance_util.find_deals()
print("Yielded interesting tickers: ", deal_list)
text_util.send_text_list(deal_list)
