import configparser

_config = configparser.ConfigParser()
_config.read('./app/config.ini')

def base_url():
    return _config['DEFAULT']['base_url']


# print(_config)
# print(_config['DEFAULT']['base_url'])

