import configparser

import pymysql


def create_connection():
    config = configparser.ConfigParser()
    config.read("./config.cfg")
    host = config['db']['host']
    port = int(config['db']['port'])
    user = config['db']['user']
    password = config['db']['password']
    db = config['db']['db']
    return pymysql.connect(host=host,
                           port=port,
                           user=user,
                           password=password,
                           db=db,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
