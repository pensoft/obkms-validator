import os

if os.getenv('ENV') == 'development':
    from config.default import config
else:
    from config.production import config
    
class Config():
    
    def __init__(self, config):
        self.config = config
    
    @staticmethod
    def flatten(dictionary, parent_key='', separator='.'):
        items = []
        for key, value in dictionary.items():
            new_key = parent_key + separator + key if parent_key else key
            if isinstance(value, dict):
                items.extend(Config.flatten(value, new_key, separator=separator).items())
            else:
                items.append((new_key, value))
        return dict(items)

    def get(self, key, default=None):
        config = Config.flatten(self.config)
        if not key in config:
            return default
        return config[key]
        
config = Config(config)