from twilio.rest import Client
from config.config_util import config_util

class TextUtil:
    def __init__(self):
        self.text_creds = config_util.data_map
        self.client = Client(text_creds['account_sid'], text_creds['auth_token'])

    def send_text(self, string: stock):
        text_body = "Check out " + stock
        message = self.client.messages \
            .create(
                 body = text_body,
                 messaging_service_sid = self.text_creds['messaging_service_sid'],
                 to = self.text_creds['text_to_number'],
                 from_ = self.text_creds['text_to_number']
             )

    def send_text(self, list: stocks):
        if(len(list) == 0):
            return
        for stock in stocks:
            self.send_text(stock)

text_util = TextUtil()
