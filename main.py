""" main.py """

import sys
import logging

from app.setup_logging import setup_logger
from app.config_loader import load_config

from app.gui.gui_app import MainApp

logger = setup_logger('app', logging.INFO)



if __name__=='__main__':
    data_proces_config = load_config('./app/config.ini', 'data_proces')
    target_url = data_proces_config['target_url']

    app = MainApp(sys.argv)
    sys.exit(app.exec())