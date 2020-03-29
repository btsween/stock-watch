import yaml

class ConfigUtil:
    
    def __init__(self):
        with open('./config/config.yml') as f:
            self.data_map = yaml.safe_load(f)
            print("running ...")

config_util = ConfigUtil()
