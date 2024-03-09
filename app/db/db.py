""" module db.py """

import mysql.connector
import configparser
import os
import logging

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.DEBUG)
logger = logging.getLogger('db')

def db_connect(config_file = './config.ini'):
    config = configparser.ConfigParser()

    if os.path.exists(config_file):
        config.read(config_file)
    else:
        raise FileNotFoundError

    mysql_config = dict(config['mysql'])
    db = mysql.connector.connect(**mysql_config)
    return db

def insert_list_of_dict(data, db):
    insert_query = """
        INSERT INTO laptops (laptop_model, laptop_price, laptop_screen_size)
        VALUES (%s, %s, %s)
    """
    data_as_lot = [
        (d['laptop_model'], d['laptop_price'], d['laptop_screen_size'])
        for d in data
    ]

    try:
        with db.cursor(dictionary=True) as cursor:
            cursor.executemany(insert_query, data_as_lot)
            logger.info('Data are inserted!')
            logger.debug('data_as_lot: %s', data_as_lot)
    except mysql.connector.Error as e:
        print(e)

def main():
    laptops = [
        {
            'laptop_model':'Lenovo',
            'laptop_price': 1399,
            'laptop_screen_size': 15.6
        }
    ]

    try:
        db = db_connect()
        logger.info('Connected to db!')
    except FileNotFoundError as e:
        logger.error('Error: %s', e)

    logger.debug('Ready to inser data: %s', laptops)
    print('Ready to insert data')
    insert_list_of_dict(data = laptops, db=db)

if __name__=='__main__':
    main()        