""" module db """

import mysql.connector
import configparser
import os
import logging

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.DEBUG)
logger = logging.getLogger('db')

def db_connect(config_file = './config.ini'):
    config = configparser.ConfigParser()
    config_file = './config.ini'
        
    
    if os.path.exists(config_file):
        config.read(config_file)
    else:
        raise FileNotFoundError
    
    mysql_config = dict(config['mysql'])
    db = mysql.connector.connect(**mysql_config)
    return db

def insert_list_of_dict(data, db):
    insert_query = """
        INSERT INTO laptops (model, price, screen_size)
        VALUES (%s, %s, %s)
    """
    data = [
        (d['model'], d['price'], d['screen_size'])
        for d in data
    ]
    try:
        with db.cursor(dictionary=True) as cursor:
            cursor.executemany(insert_query, data)
            logger.info('Data are inserted!')
            logger.debug('data: %s', data)
    except mysql.connector.Error as e:
        print(e)

def main():
    laptops = [
        {
            'model':'Legion',
            'price': 2399,
            'screen_size': 16
        },
        {
            'model':'IdeaPad',
            'price': 899,
            'screen_size': 15.6
        },
        {
            'model':'V15',
            'price': 900,
            'screen_size': 15.6
        }
    ]

    try:
        db = db_connect()
        logger.info('Connected to db!')
    except FileNotFoundError as e:
        logger.error('Error: %s', e)

    logger.debug('Ready to insert data: %s', laptops)
    print('Ready to insert data')
    insert_list_of_dict(data=laptops, db=db)

if __name__=='__main__':
    main()