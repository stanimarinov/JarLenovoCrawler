import mysql.connector
import configparser
import os
import logging

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.DEBUG)
logger = logging.getLogger('load_data')

config = configparser.ConfigParser()
confid_file = './config.ini'


def db_connect(config_file = './config.ini'):
    config = configparser.ConfigParser()

    if os.path.exists(confid_file):
        config.read(confid_file)
    else:
        raise FileNotFoundError 
    
    mysql_config = dict(config['mysql'])
    db = mysql.connector.connect(**mysql_config)
    return db

def insert_list_of_dict(data, db):
    insert_query = """
        INSERT INTO lenovo (lenovo_model, lenovo_price, lenovo_screen_size)
        VALUES (%s, %s, %s)
    """
    data_as_lot = [
        (d['lenovo_model'], d['lenovo_price'], d['lenovo_screen_size'])
        for d in data
    ]
    try:
        with db.cursor(dictionary=True) as cursor:
            cursor.executemany(insert_query,data_as_lot)
            logger.info('Data are inserted!')
            logger.debug('data_as_lot: %s', data_as_lot)
    except mysql.connector.Error as e:
        print(e)   

def main():
    lenovo = [
        {
            'lenovo_model': 'IdeaPad',
            'lenovo_price': 1299 ,
            'lenovo_screen_size': 15.6
        }
    ]             