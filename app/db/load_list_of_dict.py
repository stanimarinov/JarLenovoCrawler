import mysql.connector
import configparser
import os

config = configparser.ConfigParser()
confid_file = './config.ini'

if os.path.exists(confid_file):
    config.read(confid_file)
else:
    raise FileNotFoundError 
 
mysql_config = dict(config['mysql']) 
db = mysql.connector.connect(**mysql_config) 