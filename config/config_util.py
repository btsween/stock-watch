import os

class ConfigUtil:

    def __init__(self):
        keys = ['text_to_number', 'messaging_service_sid', 'account_sid', 'text_from_number', 'auth_token']
        self.config_map = {}

        for key in keys:
            self.config_map[key] = os.environ.get(key)


config_util = ConfigUtil()
