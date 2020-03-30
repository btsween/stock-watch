from twilio.rest import Client
from config.config_util import config_util

class TextUtil:
    def __init__(self):
        self.text_creds = config_util.data_map['text_util']
        self.client = Client(self.text_creds['account_sid'], self.text_creds['auth_token'])

    def send_text(self, message):
        message = self.client.messages \
            .create(
                 body = message,
                 messaging_service_sid = self.text_creds['messaging_service_sid'],
                 to = self.text_creds['text_to_number'],
                 from_ = self.text_creds['text_from_number']
             )

    def send_text_list(self, stocks):
        if(len(stocks) == 0):
            return
        text_body = ""
        for stock in stocks:
            text_body = text_body + stock + "\n"
        self.send_text(text_body)

text_util = TextUtil()
