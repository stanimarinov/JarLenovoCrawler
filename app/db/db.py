""" module db.py """

import mysql.connector
import logging

from typing import List, Optional
from setup_logging import setup_logger
from config_loader import load_config
from types import LenovoData

logger = setup_logger("db", logging.DEBUG)

class DB:
    """Connects to a MySQL database and creating table."""

    def __init__(self, config_file: str, section: str = "mysql"):
        """ Initializes a connection to the MySQL database"""
        
        mysql_config = load_config(config_file, section=section)
        try:
            self.db = mysql.connector.connect(**mysql_config)
            logger.info("Successfull connect to MySql database '%s'", mysql_config["database"])
        except mysql.connector.Error as e:
            error_msg = f"Failed connect to MySql database: {e}"
            logger.error(error_msg)
            raise ConnectionError(error_msg) from e    

    
    def create_laptop_table(self):
        """ create 'laptop' table in database if doesn't exist."""
    
        query = """
            CREATE TABLE IF NOT EXISTS laptop (
                id INT AUTO_INCREMENT PRIMARY KEY,
                model VARCHAR(50),
                price VARCHAR(50),
                screen_size VARCHAR(50),
                created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP        
            )
        """
        with self.db.cursor() as cursor:
                try:
                    cursor.execute(query)
                    self.db.commit()
                except mysql.connector.Error as e:
                    logger.error('Error executing [%s]: %s', query, e)
    
    def insert_laptop_data(self, laptop_data: List[LenovoData]):
        """Inserts a list of Lenovo data into 'laptop' table.
            Args:
                laptop_data (List[LenovoData]):
                    list of dictionaries where each dictionary represents a Lenovo
                    with keys 'model', 'price', and 'screen_size'.
        """

        query = """
            INSERT INTO laptop (model, price, screen_size)
            VALUES (%s, %s, %s)
        """
        laptop_data_tupples = [
            (Lenovo["model"], Lenovo["price"], Lenovo["screen_size"])
            for Lenovo in laptop_data
        ]
        with self.db.cursor() as cursor:
            try:
                cursor.executemany(query, laptop_data_tupples)
                self.db.commit()
                logger.info("Successfully inserted: %s rows.", len(laptop_data))
            except mysql.connector.Error as e:
                logger.error('Error executing [%s]: %s', query, e)

    def select_all_data(self):
        """Select all data from 'laptop' table."""

        query = "SELECT * FROM laptop;"

        with self.db.cursor() as cursor:
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                logger.info("Successfully retrieved all: %s rows.", cursor.rowcount)
                logger.debug("All rows: %s",result[:10])
                return result
            except mysql.connector.Error as e:
                logger.error('Error executing [%s]: %s', query, e)  

    def get_column_names(self) -> List[str]:
        """Retrieve the column names of the 'laptop' table."""

        query = "SELECT * FROM laptop LIMIT 1;"
        column_names = []

        with self.db.cursor() as cursor:
            try:
                cursor.execute(query)
                row = cursor.fetchone()

                if row and cursor.description:
                    column_names = [desc[0] for desc in cursor.description]
                    logger.info('Column names: %s', column_names)
                else:
                    logger.warning('No rows returned by query')
            except mysql.connector.Error as e:
                logger.error('Error executing [%s]: %s', query, e)

        return column_names  

    def get_last_updated_date(self) -> Optional[str]:
        """Retrieve the last updated date from 'laptop' table."""

        query = 'SELECT MAX(updated_at) AS max_date FROM laptop;'

        with self.db.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(query)
                result = cursor.fetchone()
                if result and 'max_date' in result:
                    return result['max_date'] 
                else:
                    raise ValueError('No data in table')
            except mysql.connector.Error as e:
                logger.error('Error executing [%s]: %s', query, e) 

if __name__ == "__main__":
    db = DB("app/config.ini", section='mysql')

    data: List[LenovoData] = [
        {
            "model": "Lenovo_name1",
            "price": 1399,
            "screen_size": 14
        },
        {
            "model": "Lenovo_name2",
            "price": 1499,
            "area": 15.6
        },
    ]

    db.insert_laptop_data(data)