from twilio.rest import Client
from config.config_util import config_util

class TextUtil:
    def __init__(self):
        self.client = Client(config_util.config_map['account_sid'], config_util.config_map['auth_token'])

    def send_text(self, message):
        message = self.client.messages \
            .create(
                 body = message,
                 messaging_service_sid = config_util.config_map['messaging_service_sid'],
                 to = config_util.config_map['text_to_number'],
                 from_ = config_util.config_map['text_from_number']
             )

    def send_text_list(self, stocks):
        if(len(stocks) == 0):
            return
        text_body = ""
        for stock in stocks:
            text_body = text_body + stock + "\n"
        self.send_text(text_body)

text_util = TextUtil()
