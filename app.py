from finance.finance_util import finance_util
from messaging.text_util import text_util

deal_list = finance_util.find_deals()

text_util.send_texts(deal_list)
