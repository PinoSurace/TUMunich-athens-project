import configparser


def is_debug():
    config = configparser.ConfigParser()
    config.read("./config.cfg")
    return config["app"]["debug"] == 'True'
